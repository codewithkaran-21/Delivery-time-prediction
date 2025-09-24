from src.constants import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
import os , sys
from dataclasses import dataclass
import pandas as pd 
import numpy as np 
from sklearn.base import BaseEstimator , TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder , OneHotEncoder , StandardScaler
from sklearn.pipeline import Pipeline
from src.utils import save_obj

class Feature_Engineering(BaseEstimator , TransformerMixin):
    def __init__(self):
        logging.info("-----------------Feature Engineering Started--------------------")

    def fit(self, X, y=None):
        # Nothing to learn, return self
        return self

    def distance_numpy(self , df , lat1 , lon1 , lat2 , lon2):
        p = np.pi/180
        a = 0.5 - np.cos((df[lat2] - df[lat1])*p)/2 + np.cos(df[lat1]*p) * np.cos(df[lat2]*p) * (1-np.cos((df[lon2] - df[lon1])*p))/2

        df['distance'] = 12734 * np.arccos(a)

    def transform_data(self , df):
        try:
            logging.info("Dropping columns from the dataframe")
            df.drop(['ID'] , axis = 1 , inplace = True)
            self.distance_numpy(df , 'Restaurant_latitude',
                               'Restaurant_longitude','Delivery_location_latitude',
                                'Delivery_location_longitude')
            df.drop(columns=['Delivery_person_ID' , 'Restaurant_latitude','Restaurant_longitude','Delivery_location_latitude',
                    'Delivery_location_longitude','Order_Date','Time_Orderd','Time_Order_picked'] , axis =1 , inplace = True)
            logging.info("dropped columns succesfully from orignal dataset")

            return df
        except Exception as e:
            raise CustomException(e,sys)
    def transform(self , X : pd.DataFrame , y = None):
        try : 
            transfomed_df = self.transform_data(X)
            return transfomed_df 
        except Exception as e:
            raise CustomException(e,sys)

@dataclass 
class DataTransformationConfig():
    processed_obj_file_path = PREPROCESSING_OBJ_FILE
    tarnsform_train_file_path = TRANSFORM_TRAIN_FILE_PATH
    tarnsform_test_file_path = TRANSFORM_TEST_FILE_PATH
    feature_engg_obj_path = FEATURE_ENGG_OBJ_FILE_PATH

class DataTransformation():
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_obj(Self):
        try:
            Road_traffic_density  =['Low' ,'Medium' , 'High' , 'Jam']
            Weather_conditions = ['Sunny' , 'Cloudy' , 'Fog' , 'Sandstorms' , 'Windy' , 'Stormy']
            categorical_columns = ['Type_of_order','Type_of_vehicle','Festival' , 'City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_columns = ['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition', 'multiple_deliveries' , 'distance']
            numerical_pipeline = Pipeline(
                steps=[('impute' , SimpleImputer(strategy='constant',fill_value=0)),
                       ('scaler' , StandardScaler(with_mean=False))])
            
            categorical_pipeline = Pipeline(steps=[
                ('impute' , SimpleImputer(strategy='most_frequent')),
                ('onehot' , OneHotEncoder(handle_unknown='ignore')),
                ('scaler' , StandardScaler(with_mean=False))
            ])

            ordinal_pipeline = Pipeline(steps=[('impute' , SimpleImputer(strategy='most_frequent')),
                                               ('ordinal' , OrdinalEncoder(categories= [Road_traffic_density, Weather_conditions])),
                                               ('scaler' , StandardScaler(with_mean=False))])
            
            preprocessor = ColumnTransformer([
                ('numerical_pipeline' , numerical_pipeline , numerical_columns),
                ('categorical_pipeline' , categorical_pipeline , categorical_columns),
                ('ordinal_pipeline' , ordinal_pipeline , ordinal_encoder)
            ])
            logging.info('Pipeline steps completed')
            return preprocessor

            

        except Exception as e :
            raise CustomException(e,sys)
        
    
    def get_feature_engineering_onject(self):
        try:
            feature_engineering = Pipeline(steps=[("fe" , Feature_Engineering())])
            return feature_engineering
        except Exception as e :
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self , train_path , test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Obtaining Feature Engineering steps object')
            fe_obj = self.get_feature_engineering_onject()

            train_df = fe_obj.fit_transform(train_df)
            test_df = fe_obj.transform(test_df)

            train_df.to_csv('train_data.csv')
            test_df.to_csv('test_data.csv')

            processing_obj = self.get_data_transformation_obj()

            target_columns_name = "Time_taken (min)"

            X_train = train_df.drop(columns = target_columns_name , axis =1)
            y_train = train_df[target_columns_name]

            X_test = test_df.drop(columns = target_columns_name , axis =1)
            y_test = test_df[target_columns_name]

            X_train = processing_obj.fit_transform(X_train)
            X_test = processing_obj.transform(X_test)

            train_arr = np.c_[X_train , np.array(y_train)]
            test_arr = np.c_[X_test , np.array(y_test)]

            df_train = pd.DataFrame(train_arr)
            df_test = pd.DataFrame(test_arr)

            os.makedirs(os.path.dirname(self.data_transformation_config.tarnsform_train_file_path),exist_ok=True)
            df_train.to_csv(self.data_transformation_config.tarnsform_train_file_path, index=False , header=True)

            os.makedirs(os.path.dirname(self.data_transformation_config.tarnsform_test_file_path),exist_ok=True)
            df_test.to_csv(self.data_transformation_config.tarnsform_test_file_path, index=False , header=True)

            logging.info(f"saving the feature engineering file to {PREPROCESSING_OBJ_FILE}")
            save_obj(file_path= self.data_transformation_config.processed_obj_file_path , obj= fe_obj)
    

            logging.info(f"saving the feature engineering file to {FEATURE_ENGG_OBJ_FILE_PATH}")
            save_obj(file_path= self.data_transformation_config.feature_engg_obj_path , obj= fe_obj)

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.processed_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)





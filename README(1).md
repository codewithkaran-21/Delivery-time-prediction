
# 🚚 Delivery Time Prediction  

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)  
![License](https://img.shields.io/badge/License-MIT-green.svg)  
![Stars](https://img.shields.io/github/stars/your-username/Delivery-time-prediction?style=social)  

A machine learning project to **predict delivery time** based on multiple real-world factors such as traffic, weather, distance, and order details. The project includes a full end-to-end pipeline covering data preprocessing, feature engineering, model training, evaluation, and deployment.  

---

## ⚙️ Features  

- ✅ Automated **data transformation pipeline** (handling missing values, encoding, scaling).  
- ✅ **Experiment tracking** to compare models and select the best one.  
- ✅ **Custom logging and exception handling** for better debugging and maintainability.  
- ✅ **Model training and evaluation** automated via pipeline scripts.  
- ✅ **Deployment-ready API** using `app.py` for serving predictions.  

---

## 📊 Dataset  

The project uses structured datasets for training and testing.  

- **Training Data:** `train_data.csv`  
- **Testing Data:** `test_data.csv`  

Key features include:  
- Weather conditions  
- Road traffic density  
- Distance  
- Delivery person details (age, rating, vehicle condition)  
- Type of order & type of vehicle  

Target variable: **Delivery Time**  

---

## 🚀 Getting Started  

### 🔹 1. Clone the Repository  

```bash
git clone https://github.com/your-username/Delivery-time-prediction.git
cd Delivery-time-prediction
```

### 🔹 2. Create Virtual Environment & Install Dependencies  

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate    # For Windows

pip install -r requirements.txt
```

### 🔹 3. Run Training Pipeline  

```bash
python main.py
```

### 🔹 4. Start the Application  

```bash
python app.py
```

---

## 📈 Model Training  

- Multiple ML algorithms were tested (Linear Regression, Random Forest, XGBoost, etc.).  
- The **best-performing model** was chosen based on evaluation metrics.  
- Trained model is stored for deployment and inference.  

---

## 🔗 API Usage  

Once the application is running, you can send a **POST request** to get predictions.  

### Example Request (JSON):  

```json
{
  "Weather_conditions": "Sunny",
  "Road_traffic_density": "Low",
  "Distance": 12.5,
  "Delivery_person_Age": 30,
  "Delivery_person_Rating": 4.5,
  "Vehicle_condition": 2,
  "Type_of_order": "Meal",
  "Type_of_vehicle": "Motorcycle",
  "City": "Urban"
}
```

### Example Response:  

```json
{
  "Predicted_Delivery_Time": 28.7
}
```

---

## 🛠 Tech Stack  

- Python 3.9  
- Scikit-learn  
- Pandas, NumPy  
- Flask / FastAPI (for deployment)  
- Custom Logging & Exception Handling  

---

## 📜 License  

This project is licensed under the **MIT License**.  

---

## 👤 Author  

**Karan Singh**  
📧 Contact: (add your email / LinkedIn / GitHub here)  

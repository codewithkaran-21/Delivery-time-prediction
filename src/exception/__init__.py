import os ,sys 

class CustomException(Exception):
    def __init__(self , error_message : Exception , error_details : sys):
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message ,
                                                                        error_details= error_details)

    @staticmethod
    def get_detailed_error_message(error_message : Exception , error_details : sys)->str:
        _, _, exec_tb = error_details.exc_info()
        try_block_line_number = exec_tb.tb_lineno
        exception_bloc_line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        error_message = f"""
        Error occured in script : [{file_name}]
        Try Bloc Line Number :  [{try_block_line_number}]
        Line Number :  [{exception_bloc_line_number}]
        Error Message : [{error_message}]
        """ 

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.strip()
    
  
    
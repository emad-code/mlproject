# File for exception handling

import sys   # manipulate parts of Python runtime environment
             # Any exceptions, sys has info about it
             
import logging
# import logger

# whenever error raised, this sends custom message
def error_message_detail(error, error_detail:sys):    
# ':sys' means it is present and expects from sys module
    _, _, exc_tb = error_detail.exc_info()  # details of exception
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message =  "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
        )
    
    return error_message

# Create Cutomer Exception class, inheriting from Exception
class CustomException(Exception):
    # Override init method
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        # Create error message variable
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # When printing, the error message will be printed
    def __str__(self):
        return self.error_message


# if __name__=="__main__":
    
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)
    

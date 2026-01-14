import sys
from Brain_Tumor_Detection.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Function to extract detailed error information: filename, line number, and error message.
    """
    # exc_info() returns (type, value, traceback). We only need the traceback (exc_tb).
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the name of the file where the exception occurred.
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    # Get the line number where the exception occurred.
    line_number = exc_tb.tb_lineno
    
    # Format a detailed error message string.
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    """
    Custom Exception class to handle errors with detailed context (file name and line number).
    """
    def __init__(self, error_message, error_detail: sys):
        # Inherit the base Exception class's initialization.
        super().__init__(error_message)
        
        # Generate the detailed error message using the helper function.
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        # Return the detailed error message when the exception is converted to a string.
        return self.error_message
    
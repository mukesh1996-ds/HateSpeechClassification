import os 
import sys 

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = os.path.basename(exc_tb.tb_frame.f_code.co_filename)
    error_message = "Error occurred in script: [{0}], at line: [{1}], with error: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomeException(Exception):
    def __init__(self,error_message,error_detail):
        """
        param error_message: Error message in string fromat
        """

        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
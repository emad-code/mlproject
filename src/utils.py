# File for any functionalities written in a common way
# which will be used in the entire application
# e.g. reading data from a database, the MongoDB client can be 
# made here. Saving model into the cloud, the code can be here.

import os
import sys

import numpy as np 
import pandas as pd
import dill

from src.exception import CustomException



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
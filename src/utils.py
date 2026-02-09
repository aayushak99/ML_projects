import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging	
import numpy as np

def save_object(file_path, obj):
	try:
		dir_path = os.path.dirname(file_path)
		os.makedirs(dir_path, exist_ok=True)

		with open(file_path, 'wb') as file_obj:
			pd.to_pickle(obj, file_obj)

	except Exception as e:
		logging.info('Error in save_object')
		raise CustomException(e, sys)
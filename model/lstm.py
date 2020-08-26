import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dropout, Dense, LSTM, Embedding, SpatialDropout1D
from keras.models import load_model
import h5py
import logging
import pathlib


#class to load the LSTM model
class LstmModel:

	model = None

	def __init__(self):
		#print("LSTM model class initiated")
		current_absolute_path = str(pathlib.Path(__file__).parent.absolute())
		self.model = load_model(current_absolute_path + '/model6.h5')

if __name__ == "__main__":
	print("Main function of LSTM")
	
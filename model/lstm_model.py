import tensorflow as tf
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dropout, Dense, LSTM, Masking, Embedding, SpatialDropout1D
from keras.models import load_model
import matplotlib.pyplot as plt
import h5py
import logging

class LstmModel:

	ann_model = None

	def __init__(self):
		print("LSTM model class initiated")
		lstm_model = load_model('./model2.h5')
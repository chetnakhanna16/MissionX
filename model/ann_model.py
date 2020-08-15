import tensorflow as tf
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dropout, Dense, LSTM, Masking, Embedding, SpatialDropout1D
from keras.models import load_model
import matplotlib.pyplot as plt
import h5py
import logging

class AnnModel:

	ann_model = None

	def __init__(self):
		print("ANN model class initiated")
		ann_model = load_model('./model1.h5')

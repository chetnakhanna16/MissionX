from keras.optimizers import SGD
import tensorflow as tf
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
		# self.ann_model = Sequential()

		# self.ann_model.add(Dense(128, input_shape=(len(train_X[0]),), activation='relu'))
		# self.ann_model.add(Dropout(0.2))

		# self.ann_model.add(Dense(128, activation='relu'))
		# self.ann_model.add(Dropout(0.5))

		# self.ann_model.add(Dense(len(train_y[0]), activation='softmax'))

		# sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)

		# self.ann_model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

		# hist_ann = self.ann_model.fit(np.array(train_X), np.array(train_y), epochs=100, batch_size=32, verbose=1)

		# self.ann_model.save('model1.h5', hist_ann)

		# self.logger = logging.getLogger()
		# self.logger.setLevel(logging.INFO)
		# self.logger.addHandler(logging.StreamHandler())
		# self.logger.INFO("ANN model is saved.")

		self.ann_model = load_model('./model1.h5')

		


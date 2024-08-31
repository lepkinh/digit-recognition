# script for loading data and training model

import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from app.model import create_model

# preparing MNIST dataset (handdrawn digits, 28x28 pixel)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# normalizing images to range of [0, 1], this will allow the model to converge faster
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# reshaping data to match Keras input format (28x28x1, the 1 channel is for grayscale)
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

# one-hot encode labels (converts class labels into a vector with a 1 at the index of the class)
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# create model
model = create_model()

# train model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=128)

# save trained model
model.save('digit_recognition_model.h5')

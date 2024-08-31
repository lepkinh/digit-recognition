import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from scipy.ndimage import rotate, shift
from model import create_model

# Function to create synthetic letter dataset
def create_letter_dataset(num_samples_per_letter=1000):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_letters = len(letters)
    x_letters = np.zeros((num_letters * num_samples_per_letter, 28, 28), dtype=np.float32)
    y_letters = np.zeros(num_letters * num_samples_per_letter, dtype=np.int32)
    
    for i, letter in enumerate(letters):
        for j in range(num_samples_per_letter):
            image = np.zeros((28, 28), dtype=np.float32)
            cv2.putText(image, letter, (4, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 1, 2)
            
            # Apply random rotation and shift
            angle = np.random.uniform(-15, 15)
            sx, sy = np.random.uniform(-2, 2, 2)
            image = rotate(image, angle, reshape=False)
            image = shift(image, [sx, sy])
            
            x_letters[i * num_samples_per_letter + j] = image
            y_letters[i * num_samples_per_letter + j] = i + 10  # Start letter labels from 10
    
    return x_letters, y_letters

# Load MNIST dataset
(x_train_digits, y_train_digits), (x_test_digits, y_test_digits) = mnist.load_data()

# Create synthetic letter dataset
x_train_letters, y_train_letters = create_letter_dataset(num_samples_per_letter=1000)
x_test_letters, y_test_letters = create_letter_dataset(num_samples_per_letter=200)

# Combine digits and letters
x_train = np.concatenate([x_train_digits, x_train_letters])
y_train = np.concatenate([y_train_digits, y_train_letters])
x_test = np.concatenate([x_test_digits, x_test_letters])
y_test = np.concatenate([y_test_digits, y_test_letters])

# Normalize images to range [0, 1]
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Reshape data to match Keras input format
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

# One-hot encode labels
y_train = to_categorical(y_train, 36)
y_test = to_categorical(y_test, 36)

# Create model
model = create_model()

# Train model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20, batch_size=128)

# Save trained model
model.save('alphanumeric_recognition_model.h5')
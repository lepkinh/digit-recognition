# script for making predictions

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist

# load MNIST dataset
(_, _), (x_test, _) = mnist.load_data()

# normalize the images to the range [0, 1]
x_test = x_test.astype('float32') / 255

# reshape data to match Keras input format
x_test = x_test.reshape((-1, 28, 28, 1))

# load the trained model
model = load_model('digit_recognition_model.h5')

# make predictions on the test set
predictions = model.predict(x_test)

# plot the first test image and the model's prediction
plt.imshow(x_test[0].reshape(28, 28), cmap='gray')
plt.title(f"Predicted: {np.argmax(predictions[0])}")
plt.show()

import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist
from extra_keras_datasets import emnist
from app.model import create_model

# Load EMNIST dataset
(x_train, y_train), (x_test, y_test) = emnist.load_data(type='balanced')

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
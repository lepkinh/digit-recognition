# script for evaluating model

from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# load MNIST dataset
(_, _), (x_test, y_test) = mnist.load_data()

# normalize the images to the range [0, 1]
x_test = x_test.astype('float32') / 255

# reshape data to match Keras input format
x_test = x_test.reshape((-1, 28, 28, 1))

# one-hot encode the labels
y_test = to_categorical(y_test, 10)

# load the trained model
model = load_model('digit_recognition_model.h5')

# evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

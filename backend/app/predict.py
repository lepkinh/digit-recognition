import random
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
from train import create_letter_dataset

# Load MNIST dataset
(_, _), (x_test_digits, y_test_digits) = mnist.load_data()

# Create synthetic letter dataset
x_test_letters, y_test_letters = create_letter_dataset(num_samples_per_letter=200)

# Combine digits and letters
x_test = np.concatenate([x_test_digits, x_test_letters])
y_test = np.concatenate([y_test_digits, y_test_letters])

# Normalize the images to the range [0, 1]
x_test = x_test.astype('float32') / 255

# Reshape data to match Keras input format
x_test = x_test.reshape((-1, 28, 28, 1))

# Load the trained model
model = load_model('alphanumeric_recognition_model.h5')

# Make predictions on the test set
predictions = model.predict(x_test)

# Define a mapping from class index to character
char_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Plot some test images and the model's predictions
for _ in range(5):
    random_index = random.randint(0, len(x_test) - 1)
    plt.imshow(x_test[random_index].reshape(28, 28), cmap='gray')
    predicted_class = np.argmax(predictions[random_index])
    predicted_char = char_map[predicted_class]
    true_char = char_map[y_test[random_index]]
    plt.title(f"Predicted: {predicted_char}, True: {true_char}, img #{random_index}")
    plt.show()
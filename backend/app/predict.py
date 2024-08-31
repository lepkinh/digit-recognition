import random
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from extra_keras_datasets import emnist

# Load EMNIST dataset
(_, _), (x_test, _) = emnist.load_data(type='balanced')

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
    plt.title(f"Predicted: {predicted_char}, img #{random_index}")
    plt.show()
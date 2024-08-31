from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from extra_keras_datasets import emnist

# Load EMNIST dataset
(_, _), (x_test, y_test) = emnist.load_data(type='balanced')

# Normalize the images to the range [0, 1]
x_test = x_test.astype('float32') / 255

# Reshape data to match Keras input format
x_test = x_test.reshape((-1, 28, 28, 1))

# One-hot encode the labels
y_test = to_categorical(y_test, 36)

# Load the trained model
model = load_model('alphanumeric_recognition_model.h5')

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
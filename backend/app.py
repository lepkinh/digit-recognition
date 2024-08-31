# main Flask app

import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

# load the trained model
model = tf.keras.models.load_model('digit_recognition_model.h5')

# route to check if the API is running
@app.route('/', methods=['GET'])
def home():
    return "Digit Recognition API is Running"

# route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log incoming request
        logging.debug("Received a POST request at /predict")

        # Get the JSON data
        data = request.get_json()
        logging.debug(f"Received data: {data}")

        # Extract image data (ensure list of pixel values)
        if 'image' not in data:
            raise KeyError("No image data found in request")

        image_data = data['image']
        logging.debug("Image data received successfully")

        # Convert list to numpy array and reshape for your model (28x28 input for MNIST)
        image_array = np.array(image_data).reshape(28, 28)

        # Normalize the pixel values (0-255 -> 0-1)
        image_array = image_array / 255.0

        # Add batch dimension and channel dimension (if needed by your model)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = np.expand_dims(image_array, axis=-1)

        # Make the prediction
        prediction = model.predict(image_array)
        predicted_digit = np.argmax(prediction)

        return jsonify({'prediction': int(predicted_digit)})
    
    except KeyError as e:
        logging.error(f"KeyError: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logging.error(f"Exception: {str(e)}")
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # start the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)

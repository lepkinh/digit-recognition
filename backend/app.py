# main Flask app

from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# load the trained model
model = tf.keras.models.load_model('digit_recognition_model.h5')

# route to check if the API is running
@app.route('/', methods=['GET'])
def home():
    return "Digit Recognition API is Running"

# route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    # get the image from the POST request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found in the request'}), 400

    # read the image file
    img_file = request.files['image'].read()
    img = Image.open(io.BytesIO(img_file)).convert('L')  # Convert to grayscale

    # resize to 28x28, which is the input shape for the model
    img = img.resize((28, 28))
    
    # convert to numpy array and normalize the pixel values
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = np.expand_dims(img_array, axis=-1)  # Add channel dimension

    # make prediction
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)

    # return the prediction as JSON
    return jsonify({'prediction': int(predicted_digit)})

if __name__ == '__main__':
    # start the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)

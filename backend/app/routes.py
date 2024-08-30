# Flask routes to handle API requests

from flask import Flask, request, jsonify
from app.model import create_model
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("digit_recognition_model.h5")

@app.route('/predict', methods=['POST'])
def predict():
    # parse image data from request
    data = request.get_json()

    # flat list of pixel values***
    image_data = data['image']
    predicted_digit = predict_digit(image_data)
    return jsonify({'digit': int(predicted_digit)})

if __name__ == '__main__':
    app.run(debug=True)

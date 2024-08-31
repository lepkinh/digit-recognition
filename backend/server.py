# Description: This file contains the Flask server that will be used to serve the model and make predictions.

from flask import Flask, request, jsonify
from flask_cors import CORS
from app.predict import predict_digit
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    image = Image.open(io.BytesIO(image_file.read())).convert('L')
    image = image.resize((28, 28))
    image_array = np.array(image).reshape(-1, 28, 28, 1) / 255.0
    
    prediction = predict_digit(image_array)
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

# Handwritten Digit Recognition Web App

This project is a web application that allows users to draw a digit on a canvas, which is then processed by a machine learning model to predict the digit. The project involves a React frontend for drawing and interaction and a Flask backend for handling the prediction using a trained machine learning model.

## Features

- **Canvas Drawing**: Users can draw digits using a canvas on the webpage.
- **Digit Prediction**: The app processes the drawn digit and uses a machine learning model to predict it.
- **Clear Functionality**: Users can clear the canvas and start over.
- **Model Prediction Feedback**: The model's prediction is displayed after processing the input.


## Getting Started

### Prerequisites

To run this project locally, you'll need the following installed:

- **Python 3.x** for the backend
- **Node.js and npm** for the frontend
- **Flask** for serving the backend
- **React.js** for the frontend

### Backend Setup

1. Navigate to the `backend/` directory:

```
cd backend
```
2. Setup virtual environment
```
python3 -m venv venv
```
3. Activate the virtual environment: (Windows)
```
venv\Scripts\activate
```
4. Install the required Python packages:
```
pip install -r requirements.txt
```
5. Run Flask backend
```
python app.py
```
### Frontend setup
1. Navigate to 'frontend/'
2. Install dependencies
```
npm install
```
3. Start the React app:
```
npm start
```

## How it works
1. The user draws a digit on the canvas provided by the React frontend.
2. The drawn image is preprocessed (resized to 28x28 pixels and converted to grayscale).
3. The preprocessed image is sent to the Flask backend, where a trained machine learning model (I trained it btw) predicts the digit.
4. The prediction is sent back to the frontend and displayed to the user.

## Tools used
- Frontend: React.js, HTML5 Canvas
- Backend: Flask, Python
- Machine learning: TensorFlow/Keras, NumPy

## License
This project is licensed under the MIT License.

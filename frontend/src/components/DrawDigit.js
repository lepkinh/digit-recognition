// drawing component for index page

import React, { useState } from 'react';
import axios from 'axios';

const DrawDigit = () => {
    const [predictedDigit, setPredictedDigit] = useState(null);

    const handleSubmit = async () => {
        // Convert canvas drawing to image data
        const canvas = document.getElementById('digitCanvas');
        const context = canvas.getContext('2d');
        const imageData = context.getImageData(0, 0, 28, 28).data;

        // Send image data to backend for prediction
        const response = await axios.post('/predict', { image: imageData });
        setPredictedDigit(response.data.digit);
    };

    return (
        <div>
            <canvas id="digitCanvas" width="28" height="28" style={{ border: '1px solid black' }}></canvas>
            <button onClick={handleSubmit}>Predict</button>
            {predictedDigit !== null && <p>Predicted Digit: {predictedDigit}</p>}
        </div>
    );
};

export default DrawDigit;

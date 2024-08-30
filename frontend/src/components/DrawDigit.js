// drawing component for index page

import React, { useRef, useState } from 'react';
import axios from 'axios';

const DrawDigit = () => {
    const canvasRef = useRef(null);
    const [predictedDigit, setPredictedDigit] = useState(null);

    const handleDraw = (e) => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        ctx.stroke();
    };

    const handleMouseDown = () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.beginPath();
    };

    const handleSubmit = async () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        const imageData = ctx.getImageData(0, 0, 28, 28).data;

        // convert canvas pixel data to grayscale values
        let grayscaleData = [];
        for (let i = 0; i < imageData.length; i += 4) {
            grayscaleData.push(imageData[i]); // using the red channel (all channels should be equal in grayscale)
        }

        try {
            const response = await axios.post('/predict', { image: grayscaleData });
            setPredictedDigit(response.data.digit);
        } catch (error) {
            console.error('Error sending image data:', error);
        }
    };

    return (
        <div>
            <canvas
                ref={canvasRef}
                width="280"
                height="280"
                style={{ border: '1px solid black' }}
                onMouseMove={handleDraw}
                onMouseDown={handleMouseDown}
            ></canvas>
            <button onClick={handleSubmit}>Predict</button>
            {predictedDigit !== null && <p>Predicted Digit: {predictedDigit}</p>}
        </div>
    );
};

export default DrawDigit;


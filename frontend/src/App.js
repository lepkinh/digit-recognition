// main React app file  

import React, { useRef, useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DrawDigit from './components/DrawDigit';
import About from './components/About';
import Header from './components/Header';

function App() {
    const canvasRef = useRef(null);
    const [isDrawing, setIsDrawing] = useState(false);

    const startDrawing = (e) => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.beginPath();
        ctx.moveTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        setIsDrawing(true);
    };

    const draw = (e) => {
        if (!isDrawing) return;
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        ctx.stroke();
    };

    const stopDrawing = () => {
        setIsDrawing(false);
    };

    const sendImageDataToBackend = () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');

        // Get image data
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;

        // Preprocess image data and send to backend
        const processedData = preprocessImageData(imageData);
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ image: processedData })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Prediction result:", data.prediction);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    const preprocessImageData = (imageData) => {
        // Create a temporary canvas to resize the image
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');
        
        // Resize the canvas to 28x28 pixels (as expected by the model)
        tempCanvas.width = 28;
        tempCanvas.height = 28;
    
        // Draw the current canvas image onto the resized canvas
        tempCtx.drawImage(canvasRef.current, 0, 0, 28, 28);
    
        // Get the image data from the resized canvas (28x28)
        const resizedImageData = tempCtx.getImageData(0, 0, 28, 28).data;
    
        // Convert the image to grayscale and normalize pixel values to [0, 1]
        const grayscaleImage = [];
        for (let i = 0; i < resizedImageData.length; i += 4) {
            // Compute grayscale value by averaging the RGB values
            const grayscaleValue = resizedImageData[i] * 0.3 + resizedImageData[i + 1] * 0.59 + resizedImageData[i + 2] * 0.11;
            // Normalize grayscale value to [0, 1] range
            grayscaleImage.push(grayscaleValue / 255.0);
        }
    
        // Return the flattened grayscale image array
        return grayscaleImage;
    };
    

    return (
        <div className="App">
            <canvas
                ref={canvasRef}
                width={280}
                height={280}
                style={{ border: "1px solid black" }}
                onMouseDown={startDrawing}
                onMouseMove={draw}
                onMouseUp={stopDrawing}
                onMouseLeave={stopDrawing}
            ></canvas>
            <button onClick={sendImageDataToBackend}>Predict</button>
        </div>
    );
}

export default App;


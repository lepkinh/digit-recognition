// main React app file  

import React, { useRef, useState } from 'react';

function App() {
    const canvasRef = useRef(null);  // Reference to the canvas
    const [isDrawing, setIsDrawing] = useState(false);  // State to track drawing
    const [prediction, setPrediction] = useState(null);  // State to store prediction

    // Function to start drawing
    const startDrawing = (e) => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.beginPath();
        ctx.moveTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        setIsDrawing(true);
    };

    // Function to continue drawing as the mouse moves
    const draw = (e) => {
        if (!isDrawing) return;
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        ctx.stroke();
    };

    // Function to stop drawing
    const stopDrawing = () => {
        setIsDrawing(false);
    };

    // Function to preprocess the image data (grayscale and normalize)
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

    // Function to handle the Predict button click
    const handlePredictClick = async () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
        const preprocessedData = preprocessImageData(imageData);

        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: preprocessedData }),
        });

        const result = await response.json();
        setPrediction(result.prediction);  // Set the prediction received from the backend
    };

    // Function to handle the Clear button click
    const handleClearClick = () => {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);  // Clear the canvas
        setPrediction(null);  // Clear the prediction as well
    };

    return (
        <div className="App">
            {/* Canvas for drawing */}
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
            
            {/* Buttons for predicting and clearing */}
            <button onClick={handlePredictClick}>Predict</button>
            <button onClick={handleClearClick}>Clear</button>
            
            {/* Display the prediction result */}
            {prediction !== null && <p>Model's prediction: {prediction}</p>}
        </div>
    );
}

export default App;

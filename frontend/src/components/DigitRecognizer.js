import React, { useRef, useState } from 'react';

const DigitRecognizer = () => {
  const canvasRef = useRef(null);
  const [prediction, setPrediction] = useState(null);

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  };

  const predictDigit = async () => {
    const canvas = canvasRef.current;
    const imageDataUrl = canvas.toDataURL('image/png');
    
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      body: JSON.stringify({ image: imageDataUrl }),
      headers: { 'Content-Type': 'application/json' },
    });
    
    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div className="flex flex-col items-center">
      <canvas
        ref={canvasRef}
        width={280} // Change this to 28x28
        height={280}
        className="border border-gray-300"
      />
      <div className="mt-4 space-x-4">
        <button onClick={clearCanvas} className="px-4 py-2 bg-red-500 text-white rounded">
          Clear
        </button>
        <button onClick={predictDigit} className="px-4 py-2 bg-blue-500 text-white rounded">
          Predict
        </button>
      </div>
      {prediction !== null && (
        <div className="mt-4 text-xl">
          Predicted digit: {prediction}
        </div>
      )}
    </div>
  );
};

export default DigitRecognizer;
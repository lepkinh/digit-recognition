import React, { useRef, useState, useEffect } from 'react';

const DigitRecognizer = () => {
  const canvasRef = useRef(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.lineWidth = 15;
    ctx.lineCap = 'round';
    ctx.strokeStyle = 'black';
    clearCanvas();
  }, []);

  const drawGrid = (ctx) => {
    ctx.strokeStyle = '#e0e0e0';
    ctx.lineWidth = 1;
    
    // Draw vertical lines
    for (let i = 0; i <= 280; i += 40) {
      ctx.beginPath();
      ctx.moveTo(i, 0);
      ctx.lineTo(i, 280);
      ctx.stroke();
    }
    
    // Draw horizontal lines
    for (let i = 0; i <= 280; i += 40) {
      ctx.beginPath();
      ctx.moveTo(0, i);
      ctx.lineTo(280, i);
      ctx.stroke();
    }
    
    ctx.strokeStyle = 'black';
    ctx.lineWidth = 15;
  };

  const startDrawing = (e) => {
    const { offsetX, offsetY } = getCoordinates(e);
    setIsDrawing(true);
    const ctx = canvasRef.current.getContext('2d');
    ctx.beginPath();
    ctx.moveTo(offsetX, offsetY);
  };

  const draw = (e) => {
    if (!isDrawing) return;
    const { offsetX, offsetY } = getCoordinates(e);
    const ctx = canvasRef.current.getContext('2d');
    ctx.lineTo(offsetX, offsetY);
    ctx.stroke();
  };

  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const getCoordinates = (e) => {
    if (e.touches) {
      const rect = canvasRef.current.getBoundingClientRect();
      return {
        offsetX: e.touches[0].clientX - rect.left,
        offsetY: e.touches[0].clientY - rect.top
      };
    }
    return { offsetX: e.nativeEvent.offsetX, offsetY: e.nativeEvent.offsetY };
  };

  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    drawGrid(ctx);
    setPrediction(null);
  };

  const predictDigit = async () => {
    const canvas = canvasRef.current;
    const imageDataUrl = canvas.toDataURL('image/png');
    
    const formData = new FormData();
    formData.append('image', dataURItoBlob(imageDataUrl));

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData,
      });
      
      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error predicting digit:', error);
    }
  };

  const dataURItoBlob = (dataURI) => {
    const byteString = atob(dataURI.split(',')[1]);
    const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], {type: mimeString});
  };

  return (
    <div className="flex flex-col items-center">
      <canvas
        ref={canvasRef}
        width={280}
        height={280}
        className="border border-gray-300 touch-none"
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={stopDrawing}
        onMouseOut={stopDrawing}
        onTouchStart={startDrawing}
        onTouchMove={draw}
        onTouchEnd={stopDrawing}
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
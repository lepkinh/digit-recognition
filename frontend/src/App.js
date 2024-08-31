import './App.css';
import React from 'react';
import DigitRecognizer from './components/DigitRecognizer';

function App() {
  return (
    <div className="App">
      <h1 className="text-3xl font-bold mb-4">Digit Recognizer</h1>
      <DigitRecognizer />
    </div>
  );
}

export default App;
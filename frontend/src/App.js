// main React app file  

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DrawDigit from './components/DrawDigit';
import About from './components/About';
import Header from './components/Header';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<DrawDigit />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;

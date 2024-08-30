// main React app file

import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import DrawDigit from './components/DrawDigit';
import About from './components/About';
import Header from './components/Header';

function App() {
    return (
        <Router>
            <div>
                <Header />
                <Switch>
                    <Route path="/" exact component={DrawDigit} />
                    <Route path="/about" component={About} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;

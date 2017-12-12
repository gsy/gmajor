import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Score} from './components/Score';


class App extends Component {

  render() {
    var parser = new DOMParser();
    fetch("./little_star.xml")
      .then(response => response.text())
      .then(str => parser.parseFromString(str, "text/xml"))
      .then(doc => {console.log(doc); this.doc = doc;});

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>

        <Score />

      </div>
    );
  }
}

export default App;

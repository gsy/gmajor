import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Score} from './components/Score';


class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      doc: null
    }
  }

  /* componentWillMount() {
   *   var parser = new DOMParser();

   *   fetch("./little_star.xml")
   *     .then(response => response.text())
   *     .then(str => parser.parseFromString(str, "text/xml"))
   *     .then(doc => {console.log("got doc:", doc); this.setState({doc: doc})})
   * }*/

  /* 先看布局 */
  // Measure 本身也是布局 + content
  // Flexlayout add node
  render() {
    const {doc} = this.state
    console.log("render, doc:", doc)
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

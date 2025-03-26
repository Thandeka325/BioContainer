import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import UserDashboard from "./components/UserDashboard";
import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Edit <code>src/App.js</code> and save to reload.</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>

      {/* React Router Setup */}
      <Router>
        <Routes>
          <Route path="/dashboard" element={<UserDashboard />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

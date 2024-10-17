import React from 'react';
import './Navbar.css'; // Import the CSS for styling

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <a href="#home" className="nav-link">PDF ingestion and querying system</a>
      </div>
      <div className="navbar-brand">
      </div>
      <div className="navbar-right">
        <a href="#upload" className="nav-link">Home</a>
      </div>
    </nav>
  );
}

export default Navbar;

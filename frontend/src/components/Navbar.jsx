import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="container navbar-inner">
        <Link to="/" className="brand">
          <span className="brand-mark">T</span>
          <span>
            <strong>Technovalley Software India Pvt Ltd</strong>
            <small>A Valley of Knowledge</small>
          </span>
        </Link>

        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#about">About Us</a>
          <a href="#features">Features</a>
          <a href="#solutions">Solutions</a>
          <a href="#contact">Contact</a>
        </nav>

        <Link to="/chat" className="nav-button">
          Talk to Our Agent
        </Link>
      </div>
    </header>
  );
}

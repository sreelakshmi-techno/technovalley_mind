import robot from "../assets/robot.png";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section id="home" className="hero-section">
      <div className="container hero-grid">
        <div className="hero-content">
          <span className="eyebrow">AI • Enterprise • Innovation</span>
          <h1>
            TechValley <span>Mind</span>
          </h1>
          <p className="hero-tagline">The Smart Face of Technovalley.</p>

          <div className="hero-actions">
            <Link to="/chat" className="btn-primary">
              Talk to Our Agent
            </Link>
            <a href="#features" className="btn-secondary">
              Learn More <span>→</span>
            </a>
          </div>
        </div>

        <motion.div
          className="hero-visual"
          initial={{ opacity: 0, y: 25 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
        >
          <div className="hero-orb orb-one"></div>
          <div className="hero-orb orb-two"></div>
          <div className="hero-image-panel">
            <img
              src={robot}
              alt="TechValleyMind robot assistant"
              className="hero-robot"
            />
          </div>
        </motion.div>
      </div>
    </section>
  );
}

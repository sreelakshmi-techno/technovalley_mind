import { MessageSquare, Headphones, Sparkles } from "lucide-react";

export default function Features() {
  const features = [
    {
      icon: MessageSquare,
      title: "Instant Responses",
      desc: "Get accurate answers instantly."
    },
    {
      icon: Headphones,
      title: "Human-like Support",
      desc: "Professional help like a real employee."
    },
    {
      icon: Sparkles,
      title: "Perfect Assistance",
      desc: "Smart guidance for every user."
    }
  ];

  return (
    <section id="features" className="features-section">
      <div className="container">
        <div className="features-grid">
          {features.map((item, index) => {
            const Icon = item.icon;
            return (
              <article key={index} className="feature-card">
                <div className="feature-icon">
                  <Icon size={24} />
                </div>
                <h3>{item.title}</h3>
                <p>{item.desc}</p>
              </article>
            );
          })}
        </div>
      </div>
    </section>
  );
}

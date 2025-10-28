"use client"

import { Brain, TrendingUp, Palette, MessageSquare } from "lucide-react"
import { motion } from "framer-motion"

const features = [
  {
    icon: Brain,
    title: "Persistent Memory",
    description: "Remembers your context, goals, and projects over time. Never repeat yourself.",
    color: "text-primary",
    glow: "neon-glow-pink-soft",
    borderColor: "border-primary/20 hover:border-primary/50",
  },
  {
    icon: TrendingUp,
    title: "Startup Simulator",
    description: "Simulate business growth, funding rounds, team scaling, and metrics like a game.",
    color: "text-accent",
    glow: "neon-glow-blue-soft",
    borderColor: "border-accent/20 hover:border-accent/50",
  },
  {
    icon: Palette,
    title: "Canvas Designer",
    description: "AI-powered design space for slides, visuals, and mockups. Instant creativity.",
    color: "text-primary",
    glow: "neon-glow-pink-soft",
    borderColor: "border-primary/20 hover:border-primary/50",
  },
  {
    icon: MessageSquare,
    title: "Conversational Core",
    description: "Chat naturally with Emergent++. It brainstorms and builds alongside you.",
    color: "text-accent",
    glow: "neon-glow-blue-soft",
    borderColor: "border-accent/20 hover:border-accent/50",
  },
]

export function FeaturesGrid() {
  return (
    <section className="relative py-32 px-4">
      <div className="max-w-7xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-20"
        >
          <h2 className="text-5xl md:text-6xl font-bold mb-6 text-balance">
            Everything you need to <span className="text-primary text-glow-pink">build</span>
          </h2>
          <p className="text-xl md:text-2xl text-muted-foreground text-balance font-light">Powered by AI, designed for creators</p>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {features.map((feature, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: i * 0.1 }}
              whileHover={{ scale: 1.03, y: -5 }}
              className={`glass-strong rounded-3xl p-10 border ${feature.borderColor} ${feature.glow} transition-all duration-500 group cursor-pointer relative overflow-hidden`}
              data-testid={`feature-${feature.title.toLowerCase().replace(/\s+/g, '-')}`}
            >
              {/* Hover gradient effect */}
              <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none">
                <div className={`absolute inset-0 bg-gradient-to-br ${feature.color === 'text-primary' ? 'from-primary/10 via-transparent to-transparent' : 'from-accent/10 via-transparent to-transparent'}`} />
              </div>
              
              <div className="relative z-10">
                <div
                  className={`inline-flex p-5 rounded-2xl bg-secondary/50 backdrop-blur-sm mb-6 ${feature.color} group-hover:scale-110 transition-all duration-300 border border-white/10 ${feature.glow}`}
                >
                  <feature.icon className="w-8 h-8" />
                </div>
                <h3 className="text-3xl font-bold mb-4 group-hover:${feature.color} transition-colors">{feature.title}</h3>
                <p className="text-muted-foreground leading-relaxed text-lg font-light">{feature.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  )
}

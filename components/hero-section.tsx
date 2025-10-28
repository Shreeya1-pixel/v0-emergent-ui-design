"use client"

import { Button } from "@/components/ui/button"
import { Sparkles, Brain, Rocket, Zap } from "lucide-react"
import { motion } from "framer-motion"

export function HeroSection() {
  return (
    <section className="relative min-h-screen flex items-center justify-center px-4 py-20">
      {/* Enhanced animated gradient orbs with more intense glow */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <motion.div
          className="absolute top-1/4 left-1/4 w-[500px] h-[500px] rounded-full"
          style={{
            background: "radial-gradient(circle, rgba(255, 51, 153, 0.6), transparent 60%)",
            filter: "blur(100px)",
          }}
          animate={{
            scale: [1, 1.3, 1],
            x: [0, 60, 0],
            y: [0, 40, 0],
            opacity: [0.3, 0.5, 0.3],
          }}
          transition={{
            duration: 10,
            repeat: Number.POSITIVE_INFINITY,
            ease: "easeInOut",
          }}
        />
        <motion.div
          className="absolute bottom-1/4 right-1/4 w-[500px] h-[500px] rounded-full"
          style={{
            background: "radial-gradient(circle, rgba(51, 153, 255, 0.6), transparent 60%)",
            filter: "blur(100px)",
          }}
          animate={{
            scale: [1, 1.4, 1],
            x: [0, -60, 0],
            y: [0, -40, 0],
            opacity: [0.3, 0.5, 0.3],
          }}
          transition={{
            duration: 12,
            repeat: Number.POSITIVE_INFINITY,
            ease: "easeInOut",
          }}
        />
        <motion.div
          className="absolute top-1/2 right-1/3 w-[400px] h-[400px] rounded-full"
          style={{
            background: "radial-gradient(circle, rgba(200, 100, 255, 0.4), transparent 70%)",
            filter: "blur(90px)",
          }}
          animate={{
            scale: [1, 1.2, 1],
            x: [0, 40, 0],
            y: [0, -30, 0],
            opacity: [0.2, 0.4, 0.2],
          }}
          transition={{
            duration: 14,
            repeat: Number.POSITIVE_INFINITY,
            ease: "easeInOut",
          }}
        />
      </div>

      <div className="relative z-10 max-w-5xl mx-auto text-center space-y-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full glass-strong border border-primary/40 text-sm text-primary neon-glow-pink-soft"
        >
          <Sparkles className="w-4 h-4 animate-pulse" />
          <span className="font-semibold">Your AI Co-Founder</span>
          <Zap className="w-4 h-4 animate-pulse" />
        </motion.div>

        <motion.h1
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.1 }}
          className="text-6xl md:text-8xl lg:text-9xl font-bold tracking-tight text-balance leading-none"
        >
          <span className="text-glow-pink text-primary">Emergent</span>
          <span className="text-glow-blue text-accent">++</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="text-xl md:text-2xl text-muted-foreground max-w-3xl mx-auto text-balance leading-relaxed font-light"
        >
          An intelligent AI workspace that <span className="text-primary font-medium">remembers</span>, <span className="text-accent font-medium">brainstorms</span>, simulates, and designs with you. Your creative co-founder for building the future.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.3 }}
          className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4"
        >
          <Button
            size="lg"
            className="neon-glow-pink bg-primary hover:bg-primary/90 text-primary-foreground px-10 py-7 text-lg rounded-2xl transition-all duration-300 hover:scale-105 hover:shadow-2xl group"
            data-testid="start-building-btn"
          >
            <Brain className="w-5 h-5 mr-2 group-hover:scale-110 transition-transform" />
            Start Building
          </Button>
          <Button
            size="lg"
            variant="outline"
            className="glass-strong border-accent/50 hover:border-accent text-foreground px-10 py-7 text-lg rounded-2xl transition-all duration-300 hover:scale-105 bg-transparent neon-glow-blue-soft group"
            data-testid="explore-features-btn"
          >
            <Rocket className="w-5 h-5 mr-2 group-hover:scale-110 transition-transform" />
            Explore Features
          </Button>
        </motion.div>

        {/* Enhanced Stats with better glassmorphism */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="grid grid-cols-3 gap-6 pt-20 max-w-3xl mx-auto"
        >
          {[
            { label: "Ideas Stored", value: "10K+", color: "primary" },
            { label: "Startups Simulated", value: "5K+", color: "accent" },
            { label: "Designs Created", value: "25K+", color: "primary" },
          ].map((stat, i) => (
            <motion.div 
              key={i} 
              className="glass-strong rounded-2xl p-8 border border-white/10 hover:border-primary/30 transition-all duration-300 hover:scale-105 neon-glow-soft group cursor-pointer"
              whileHover={{ y: -5 }}
              data-testid={`stat-${stat.label.toLowerCase().replace(/\s+/g, '-')}`}
            >
              <div className={`text-4xl font-bold ${stat.color === 'primary' ? 'text-primary text-glow-pink' : 'text-accent text-glow-blue'} group-hover:scale-110 transition-transform`}>
                {stat.value}
              </div>
              <div className="text-sm text-muted-foreground mt-2 font-medium">{stat.label}</div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  )
}

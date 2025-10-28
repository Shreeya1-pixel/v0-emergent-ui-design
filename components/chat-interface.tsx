"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Send, Sparkles } from "lucide-react"
import { motion, AnimatePresence } from "framer-motion"

export function ChatInterface() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hey! I'm Emergent++, your AI co-founder. What are we building today?",
    },
  ])
  const [input, setInput] = useState("")

  const handleSend = () => {
    if (!input.trim()) return

    setMessages([...messages, { role: "user", content: input }])
    setInput("")

    // Simulate AI response
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: "I'm processing your idea and storing it in memory. Let's break this down into actionable steps...",
        },
      ])
    }, 1000)
  }

  return (
    <section className="relative py-32 px-4">
      <div className="max-w-4xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h2 className="text-5xl md:text-6xl font-bold mb-6 text-balance">
            Start <span className="text-accent text-glow-blue">conversing</span>
          </h2>
          <p className="text-xl md:text-2xl text-muted-foreground text-balance font-light">Your AI workspace is ready</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="glass-strong rounded-3xl border border-white/10 overflow-hidden shadow-2xl neon-glow-soft"
          data-testid="chat-interface"
        >
          {/* Chat messages */}
          <div className="h-[500px] overflow-y-auto p-8 space-y-6 custom-scrollbar">
            <AnimatePresence>
              {messages.map((message, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3 }}
                  className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
                >
                  <div
                    className={`max-w-[85%] rounded-2xl px-6 py-5 transition-all duration-300 ${
                      message.role === "user"
                        ? "bg-primary text-primary-foreground neon-glow-pink-soft hover:scale-[1.02]"
                        : "glass-strong border border-accent/30 neon-glow-blue-soft hover:scale-[1.02]"
                    }`}
                    data-testid={`message-${message.role}`}
                  >
                    {message.role === "assistant" && (
                      <div className="flex items-center gap-2 mb-3">
                        <Sparkles className="w-4 h-4 text-accent animate-pulse" />
                        <span className="text-xs font-semibold text-accent tracking-wide">EMERGENT++</span>
                      </div>
                    )}
                    <p className="leading-relaxed text-base">{message.content}</p>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>

          {/* Input area */}
          <div className="border-t border-white/10 p-6 bg-secondary/30 backdrop-blur-xl">
            <div className="flex gap-4">
              <Input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleSend()}
                placeholder="Describe your startup idea..."
                className="glass-strong border-white/20 focus:border-primary/50 bg-background/50 text-foreground placeholder:text-muted-foreground rounded-xl px-6 py-7 text-base transition-all duration-300 focus:neon-glow-pink-soft"
                data-testid="chat-input"
              />
              <Button
                onClick={handleSend}
                size="lg"
                className="neon-glow-pink bg-primary hover:bg-primary/90 text-primary-foreground rounded-xl px-10 transition-all duration-300 hover:scale-105 hover:shadow-2xl"
                data-testid="chat-send-btn"
              >
                <Send className="w-5 h-5" />
              </Button>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  )
}

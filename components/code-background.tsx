"use client"

import { useRef } from "react"

export function CodeBackground() {
  const videoRef = useRef<HTMLVideoElement>(null)

  return (
    <div className="fixed inset-0 w-full h-full pointer-events-none overflow-hidden">
      {/* Relying solely on HTML attributes for autoplay, which is more reliable */}
      <video
        ref={videoRef}
        autoPlay
        loop
        muted
        playsInline
        preload="auto"
        className="absolute inset-0 w-full h-full object-cover opacity-80" // Increased opacity
        key="local-video-player-simple"
      >
        <source src="/codepic.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      {/* Lighter gradient overlays for readability while keeping video visible */}
      <div className="absolute inset-0 bg-gradient-to-b from-background/50 via-background/20 to-background/60" />
      <div className="absolute inset-0 bg-gradient-radial from-transparent via-background/10 to-background/50" />
      {/* Subtle noise texture for premium feel */}
      <div className="absolute inset-0 opacity-[0.02] mix-blend-overlay bg-noise" />
    </div>
  )
}

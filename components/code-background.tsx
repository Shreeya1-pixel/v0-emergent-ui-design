"use client"

import { useEffect, useRef } from "react"

export function CodeBackground() {
  const videoRef = useRef<HTMLVideoElement>(null)

  useEffect(() => {
    // Ensure video plays on component mount
    if (videoRef.current) {
      videoRef.current.play().catch((error) => {
        console.log("Video autoplay prevented:", error)
      })
    }
  }, [])

  return (
    <div className="fixed inset-0 w-full h-full pointer-events-none overflow-hidden">
      {/* User's uploaded video background - More prominent */}
      <video 
        ref={videoRef}
        autoPlay 
        loop 
        muted 
        playsInline
        preload="auto"
        className="absolute inset-0 w-full h-full object-cover opacity-70"
      >
        <source src="https://customer-assets.emergentagent.com/job_1215c7b6-2b8a-4bbc-9193-b67c01d86604/artifacts/sh6lbx3r_c1.mp4" type="video/mp4" />
      </video>
      {/* Lighter gradient overlays for readability while keeping video visible */}
      <div className="absolute inset-0 bg-gradient-to-b from-background/60 via-background/30 to-background/70" />
      <div className="absolute inset-0 bg-gradient-radial from-transparent via-background/20 to-background/60" />
      {/* Subtle noise texture for premium feel */}
      <div className="absolute inset-0 opacity-[0.02] mix-blend-overlay bg-noise" />
    </div>
  )
}

"use client"

export function CodeBackground() {
  return (
    <div className="fixed inset-0 w-full h-full pointer-events-none overflow-hidden">
      {/* User's uploaded video background */}
      <video 
        autoPlay 
        loop 
        muted 
        playsInline 
        className="absolute inset-0 w-full h-full object-cover opacity-30"
      >
        <source src="https://customer-assets.emergentagent.com/job_1215c7b6-2b8a-4bbc-9193-b67c01d86604/artifacts/sh6lbx3r_c1.mp4" type="video/mp4" />
      </video>
      {/* Multi-layer gradient overlays for depth */}
      <div className="absolute inset-0 bg-gradient-to-b from-background/80 via-background/50 to-background" />
      <div className="absolute inset-0 bg-gradient-radial from-transparent via-background/30 to-background" />
      {/* Subtle noise texture for premium feel */}
      <div className="absolute inset-0 opacity-[0.015] mix-blend-overlay bg-noise" />
    </div>
  )
}

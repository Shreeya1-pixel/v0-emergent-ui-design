from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from models import (
    ChatRequest, MemoryRequest, StartupRequest, 
    SimulateRequest, DesignRequest, Message, Memory, Startup, Design
)
from services.ai_service import ai_service
from services.memory_service import memory_service
from services.startup_service import startup_service
from services.canvas_service import design_service, conversation_service

# Load environment variables
load_dotenv()

app = FastAPI(title="Emergent++ API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "Emergent++ Backend"}

# ============ CHAT ENDPOINTS ============

@app.post("/api/chat")
async def chat(request: ChatRequest):
    """
    Chat with Emergent++ AI co-founder
    Maintains conversation context and memory
    """
    try:
        # Get conversation history
        history = await conversation_service.get_conversation_history(
            request.session_id, limit=10
        )
        
        # Add user message
        user_message = Message(role="user", content=request.message)
        await conversation_service.add_message(request.session_id, user_message)
        
        # Prepare messages for AI
        all_messages = history + [user_message]
        
        # Get AI response
        system_prompt = """
You are Emergent++, an intelligent AI co-founder workspace.
You help users:
- Brainstorm and develop ideas
- Plan and simulate startups
- Create designs and visuals
- Remember context and build on previous conversations

Be creative, insightful, and actionable. Help users turn ideas into reality.
"""
        
        response_content = await ai_service.chat_completion(
            all_messages, 
            system_prompt=system_prompt,
            user_api_key=request.user_api_key
        )
        
        # Save assistant response
        assistant_message = Message(role="assistant", content=response_content)
        await conversation_service.add_message(request.session_id, assistant_message)
        
        return {
            "response": response_content,
            "session_id": request.session_id
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/chat/history/{session_id}")
async def get_chat_history(session_id: str, limit: int = 20):
    """Get conversation history"""
    try:
        history = await conversation_service.get_conversation_history(session_id, limit)
        return {"messages": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ MEMORY ENDPOINTS ============

@app.post("/api/memory")
async def create_memory(request: MemoryRequest):
    """Create a new memory entry"""
    try:
        memory = Memory(
            session_id=request.session_id,
            content=request.content,
            category=request.category,
            tags=request.tags
        )
        result = await memory_service.create_memory(memory)
        return {"success": True, "memory": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/memory/{session_id}")
async def get_memories(session_id: str, category: str = None):
    """Get all memories for a session"""
    try:
        memories = await memory_service.get_memories(session_id, category)
        return {"memories": memories, "count": len(memories)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/memory/search/{session_id}")
async def search_memories(session_id: str, q: str):
    """Search memories"""
    try:
        memories = await memory_service.search_memories(session_id, q)
        return {"memories": memories, "count": len(memories)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/memory/{memory_id}")
async def delete_memory(memory_id: str):
    """Delete a memory"""
    try:
        success = await memory_service.delete_memory(memory_id)
        return {"success": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ STARTUP SIMULATOR ENDPOINTS ============

@app.post("/api/startup")
async def create_startup(request: StartupRequest):
    """Create a new startup simulation"""
    try:
        startup = Startup(
            session_id=request.session_id,
            name=request.name,
            description=request.description,
            stage="idea"
        )
        result = await startup_service.create_startup(startup)
        return {"success": True, "startup": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/startup/{session_id}")
async def get_startups(session_id: str):
    """Get all startups for a session"""
    try:
        startups = await startup_service.get_startups(session_id)
        return {"startups": startups, "count": len(startups)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/startup/detail/{startup_id}")
async def get_startup_detail(startup_id: str):
    """Get specific startup details"""
    try:
        startup = await startup_service.get_startup(startup_id)
        if not startup:
            raise HTTPException(status_code=404, detail="Startup not found")
        return {"startup": startup}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/startup/simulate")
async def simulate_startup(request: SimulateRequest):
    """Simulate startup growth"""
    try:
        # Get startup details
        startup = await startup_service.get_startup(request.startup_id)
        if not startup:
            raise HTTPException(status_code=404, detail="Startup not found")
        
        # Generate simulation
        simulation = await ai_service.generate_startup_simulation(
            startup.name,
            startup.description,
            startup.stage,
            request.months,
            user_api_key=request.user_api_key
        )
        
        return {
            "success": True,
            "startup_id": request.startup_id,
            "simulation": simulation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/startup/{startup_id}")
async def delete_startup(startup_id: str):
    """Delete a startup"""
    try:
        success = await startup_service.delete_startup(startup_id)
        return {"success": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ CANVAS DESIGNER ENDPOINTS ============

@app.post("/api/canvas/generate")
async def generate_design(request: DesignRequest):
    """Generate AI-powered design"""
    try:
        # Generate image with DALL-E
        image_url = await ai_service.generate_design_image(
            request.prompt,
            request.design_type,
            user_api_key=request.user_api_key
        )
        
        # Save design
        design = Design(
            session_id=request.session_id,
            title=f"{request.design_type.title()} Design",
            prompt=request.prompt,
            image_url=image_url,
            design_type=request.design_type
        )
        result = await design_service.create_design(design)
        
        return {
            "success": True,
            "design": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/canvas/{session_id}")
async def get_designs(session_id: str):
    """Get all designs for a session"""
    try:
        designs = await design_service.get_designs(session_id)
        return {"designs": designs, "count": len(designs)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/canvas/{design_id}")
async def delete_design(design_id: str):
    """Delete a design"""
    try:
        success = await design_service.delete_design(design_id)
        return {"success": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ SESSION MANAGEMENT ============

@app.get("/api/session/{session_id}/summary")
async def get_session_summary(session_id: str):
    """Get complete session summary"""
    try:
        memories = await memory_service.get_memories(session_id)
        startups = await startup_service.get_startups(session_id)
        designs = await design_service.get_designs(session_id)
        history = await conversation_service.get_conversation_history(session_id)
        
        return {
            "session_id": session_id,
            "memories_count": len(memories),
            "startups_count": len(startups),
            "designs_count": len(designs),
            "messages_count": len(history),
            "summary": {
                "memories": memories[:5],  # Latest 5
                "startups": startups[:3],  # Latest 3
                "designs": designs[:5]  # Latest 5
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

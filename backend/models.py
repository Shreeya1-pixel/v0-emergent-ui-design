from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from uuid import uuid4

def generate_uuid():
    return str(uuid4())

class Message(BaseModel):
    role: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)

class Memory(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    content: str
    category: str  # idea, goal, project, note
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Conversation(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    messages: List[Message] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class StartupMetrics(BaseModel):
    users: int = 0
    revenue: float = 0.0
    funding: float = 0.0
    team_size: int = 1
    growth_rate: float = 0.0

class Startup(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    name: str
    description: str
    stage: str  # idea, mvp, launch, growth, scale
    metrics: StartupMetrics = Field(default_factory=StartupMetrics)
    milestones: List[Dict[str, Any]] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Design(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    title: str
    prompt: str
    image_url: Optional[str] = None
    design_type: str  # slide, mockup, visual, logo
    created_at: datetime = Field(default_factory=datetime.now)

class ChatRequest(BaseModel):
    message: str
    session_id: str
    user_api_key: Optional[str] = None

class MemoryRequest(BaseModel):
    session_id: str
    content: str
    category: str
    tags: List[str] = []

class StartupRequest(BaseModel):
    session_id: str
    name: str
    description: str
    user_api_key: Optional[str] = None

class SimulateRequest(BaseModel):
    startup_id: str
    months: int = 6
    user_api_key: Optional[str] = None

class DesignRequest(BaseModel):
    session_id: str
    prompt: str
    design_type: str
    user_api_key: Optional[str] = None

class Agent(BaseModel):
    agent_id: str
    role: str  # CEO, Engineer, Designer, Marketer
    personality: str

class AgentMessage(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    agent_id: str
    role: str  # CEO, Engineer, Designer, Marketer
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)
    to_agent_id: Optional[str] = None  # For message passing
    meta: Optional[dict] = None  # Any extra context

class AgentMemory(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    session_id: str
    agent_id: str
    log: List[AgentMessage] = []
    updated_at: datetime = Field(default_factory=datetime.now)

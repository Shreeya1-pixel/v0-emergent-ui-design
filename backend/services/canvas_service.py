from pymongo import MongoClient
from typing import List
from models import Design, Conversation, Message
from datetime import datetime
import os

class DesignService:
    def __init__(self):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.getenv("DATABASE_NAME", "emergent_plus")
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db["designs"]
    
    async def create_design(self, design: Design) -> Design:
        """Create new design"""
        design_dict = design.model_dump()
        self.collection.insert_one(design_dict)
        return design
    
    async def get_designs(self, session_id: str) -> List[Design]:
        """Get all designs for a session"""
        designs = list(self.collection.find({"session_id": session_id}).sort("created_at", -1))
        return [Design(**{**d, "_id": str(d["_id"])}) for d in designs]
    
    async def delete_design(self, design_id: str) -> bool:
        """Delete design"""
        result = self.collection.delete_one({"id": design_id})
        return result.deleted_count > 0

class ConversationService:
    def __init__(self):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.getenv("DATABASE_NAME", "emergent_plus")
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db["conversations"]
    
    async def get_or_create_conversation(self, session_id: str) -> Conversation:
        """Get existing conversation or create new one"""
        conversation = self.collection.find_one({"session_id": session_id})
        if conversation:
            return Conversation(**{**conversation, "_id": str(conversation["_id"])})
        
        # Create new conversation
        new_conv = Conversation(session_id=session_id)
        self.collection.insert_one(new_conv.model_dump())
        return new_conv
    
    async def add_message(self, session_id: str, message: Message) -> bool:
        """Add message to conversation"""
        result = self.collection.update_one(
            {"session_id": session_id},
            {
                "$push": {"messages": message.model_dump()},
                "$set": {"updated_at": datetime.now()}
            },
            upsert=True
        )
        return result.modified_count > 0 or result.upserted_id is not None
    
    async def get_conversation_history(self, session_id: str, limit: int = 10) -> List[Message]:
        """Get recent conversation history"""
        conversation = self.collection.find_one({"session_id": session_id})
        if conversation and "messages" in conversation:
            messages = conversation["messages"][-limit:]
            return [Message(**msg) for msg in messages]
        return []

design_service = DesignService()
conversation_service = ConversationService()

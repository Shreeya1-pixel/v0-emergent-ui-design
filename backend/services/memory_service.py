from pymongo import MongoClient
from typing import List, Optional
from models import Memory
from datetime import datetime
import os

class MemoryService:
    def __init__(self):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.getenv("DATABASE_NAME", "emergent_plus")
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db["memories"]
    
    async def create_memory(self, memory: Memory) -> Memory:
        """Create new memory"""
        memory_dict = memory.model_dump()
        self.collection.insert_one(memory_dict)
        return memory
    
    async def get_memories(self, session_id: str, category: Optional[str] = None) -> List[Memory]:
        """Get memories for a session"""
        query = {"session_id": session_id}
        if category:
            query["category"] = category
        
        memories = list(self.collection.find(query).sort("created_at", -1))
        return [Memory(**{**mem, "_id": str(mem["_id"])}) for mem in memories]
    
    async def search_memories(self, session_id: str, search_term: str) -> List[Memory]:
        """Search memories by content"""
        query = {
            "session_id": session_id,
            "$or": [
                {"content": {"$regex": search_term, "$options": "i"}},
                {"tags": {"$in": [search_term]}}
            ]
        }
        memories = list(self.collection.find(query).sort("created_at", -1))
        return [Memory(**{**mem, "_id": str(mem["_id"])}) for mem in memories]
    
    async def update_memory(self, memory_id: str, content: str, tags: List[str]) -> bool:
        """Update memory"""
        result = self.collection.update_one(
            {"id": memory_id},
            {"$set": {"content": content, "tags": tags, "updated_at": datetime.now()}}
        )
        return result.modified_count > 0
    
    async def delete_memory(self, memory_id: str) -> bool:
        """Delete memory"""
        result = self.collection.delete_one({"id": memory_id})
        return result.deleted_count > 0

memory_service = MemoryService()

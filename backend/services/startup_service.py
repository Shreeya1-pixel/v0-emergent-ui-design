from pymongo import MongoClient
from typing import List, Optional
from models import Startup, StartupMetrics
from datetime import datetime
import os

class StartupService:
    def __init__(self):
        mongo_url = os.getenv("MONGO_URL", "mongodb://localhost:27017")
        db_name = os.getenv("DATABASE_NAME", "emergent_plus")
        self.client = MongoClient(mongo_url)
        self.db = self.client[db_name]
        self.collection = self.db["startups"]
    
    async def create_startup(self, startup: Startup) -> Startup:
        """Create new startup"""
        startup_dict = startup.model_dump()
        self.collection.insert_one(startup_dict)
        return startup
    
    async def get_startups(self, session_id: str) -> List[Startup]:
        """Get all startups for a session"""
        startups = list(self.collection.find({"session_id": session_id}).sort("created_at", -1))
        return [Startup(**{**s, "_id": str(s["_id"])}) for s in startups]
    
    async def get_startup(self, startup_id: str) -> Optional[Startup]:
        """Get specific startup"""
        startup = self.collection.find_one({"id": startup_id})
        if startup:
            return Startup(**{**startup, "_id": str(startup["_id"])})
        return None
    
    async def update_metrics(self, startup_id: str, metrics: StartupMetrics) -> bool:
        """Update startup metrics"""
        result = self.collection.update_one(
            {"id": startup_id},
            {"$set": {"metrics": metrics.model_dump(), "updated_at": datetime.now()}}
        )
        return result.modified_count > 0
    
    async def add_milestone(self, startup_id: str, milestone: dict) -> bool:
        """Add milestone to startup"""
        result = self.collection.update_one(
            {"id": startup_id},
            {"$push": {"milestones": milestone}, "$set": {"updated_at": datetime.now()}}
        )
        return result.modified_count > 0
    
    async def update_stage(self, startup_id: str, stage: str) -> bool:
        """Update startup stage"""
        result = self.collection.update_one(
            {"id": startup_id},
            {"$set": {"stage": stage, "updated_at": datetime.now()}}
        )
        return result.modified_count > 0
    
    async def delete_startup(self, startup_id: str) -> bool:
        """Delete startup"""
        result = self.collection.delete_one({"id": startup_id})
        return result.deleted_count > 0

startup_service = StartupService()

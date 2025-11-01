import os
from openai import OpenAI
from typing import List, Optional
from models import Message

class AIService:
    def __init__(self):
        # Will use either user's API key or Emergent LLM key
        self.default_api_key = os.getenv("OPENAI_API_KEY")
    
    def get_client(self, user_api_key: Optional[str] = None) -> OpenAI:
        """Get OpenAI client with user's key or default key"""
        api_key = user_api_key or self.default_api_key
        if not api_key:
            raise ValueError("No API key provided. Please provide your OpenAI API key or configure system key.")
        return OpenAI(api_key=api_key)
    
    async def chat_completion(
        self,
        messages: List[Message],
        system_prompt: str = "You are Emergent++, an intelligent AI co-founder that helps users brainstorm, plan, and build their ideas.",
        user_api_key: Optional[str] = None
    ) -> str:
        """Generate chat completion with context"""
        try:
            client = self.get_client(user_api_key)
            
            # Format messages for OpenAI
            formatted_messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            for msg in messages:
                formatted_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=formatted_messages,
                temperature=0.7,
                max_tokens=1000
            )
            
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"AI Service Error: {str(e)}")
    
    async def generate_startup_simulation(
        self,
        startup_name: str,
        description: str,
        current_stage: str,
        months: int,
        user_api_key: Optional[str] = None
    ) -> dict:
        """Generate realistic startup growth simulation"""
        try:
            client = self.get_client(user_api_key)
            
            prompt = f"""
You are a startup growth simulator. Generate a realistic {months}-month growth projection for:

Startup: {startup_name}
Description: {description}
Current Stage: {current_stage}

Provide realistic metrics for each month including:
- Users/customers growth
- Revenue (if applicable)
- Team size
- Key milestones
- Challenges faced
- Funding events (if any)

Respond in JSON format with monthly data.
"""
            
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=2000
            )
            
            return {"simulation": response.choices[0].message.content}
        except Exception as e:
            raise Exception(f"Simulation Error: {str(e)}")
    
    async def generate_design_image(
        self,
        prompt: str,
        design_type: str,
        user_api_key: Optional[str] = None
    ) -> str:
        """Generate design image using DALL-E"""
        try:
            client = self.get_client(user_api_key)
            
            # Enhance prompt based on design type
            enhanced_prompt = f"{design_type} design: {prompt}. Professional, modern, clean aesthetic."
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=enhanced_prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            
            return response.data[0].url
        except Exception as e:
            raise Exception(f"Design Generation Error: {str(e)}")

    async def agent_chat(
        self,
        agent_role: str,
        agent_personality: str,
        task: str,
        memory_log: str = "",
        user_api_key: Optional[str] = None,
        context: Optional[str] = None,
    ) -> str:
        """Generate agent-specific response using provided personality and context."""
        try:
            client = self.get_client(user_api_key)
            system_prompt = (
                f"You are {agent_role}, one of several collaborating AI startup team experts. Your personality: {agent_personality}. "
                f"The task: {task}. "
                f"Here is your memory buffer (recent log): {memory_log}. "
            )
            if context:
                system_prompt += f"Context from teammates: {context}. "
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": system_prompt}],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Agent LLM Error: {str(e)}")

ai_service = AIService()

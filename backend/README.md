# Emergent++ Backend

A comprehensive FastAPI backend for the Emergent++ AI workspace platform.

## Features

🧠 **Conversational AI with Memory** - Chat with AI that remembers your context
💾 **Persistent Memory Storage** - Store ideas, goals, and projects with MongoDB
🚀 **Startup Simulator** - Create and simulate startup growth
🎨 **Canvas Designer** - Generate AI-powered designs with DALL-E

## Tech Stack

- **FastAPI** - Modern Python web framework
- **MongoDB** - Document database for flexible data storage
- **OpenAI GPT-4o** - Conversational AI
- **OpenAI DALL-E 3** - AI image generation
- **Pydantic** - Data validation

## Project Structure

```
backend/
├── server.py              # Main FastAPI application
├── models.py              # Pydantic models & schemas
├── services/
│   ├── ai_service.py      # OpenAI integration
│   ├── memory_service.py  # Memory management
│   ├── startup_service.py # Startup simulation
│   └── canvas_service.py  # Design generation
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── API_DOCUMENTATION.md   # Complete API docs
```

## Setup

### 1. Install Dependencies

```bash
cd /app/backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Edit `.env` file:

```env
MONGO_URL=mongodb://localhost:27017
DATABASE_NAME=emergent_plus
OPENAI_API_KEY=sk-your-key-here  # Optional: Users can provide their own
```

### 3. Start MongoDB

MongoDB should be running on `localhost:27017`

### 4. Run the Server

```bash
# Development
uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Production
uvicorn server:app --host 0.0.0.0 --port 8001 --workers 4
```

## API Key Configuration

### Option 1: User's Own API Key (Recommended)
Users can pass their OpenAI API key in each request:

```json
{
  "message": "Hello",
  "session_id": "user-123",
  "user_api_key": "sk-..."
}
```

### Option 2: System Default Key
Set `OPENAI_API_KEY` in `.env` file for all users.

### Option 3: Emergent LLM Key
Configure Emergent universal key for multi-provider support.

## API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/chat` | Chat with AI |
| GET | `/api/chat/history/{session_id}` | Get chat history |
| POST | `/api/memory` | Create memory |
| GET | `/api/memory/{session_id}` | Get memories |
| POST | `/api/startup` | Create startup |
| POST | `/api/startup/simulate` | Simulate growth |
| POST | `/api/canvas/generate` | Generate design |
| GET | `/api/session/{session_id}/summary` | Session summary |

📖 **Full API Documentation:** See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

## Quick Test

```bash
# Health check
curl http://localhost:8001/api/health

# Create a memory
curl -X POST http://localhost:8001/api/memory \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "demo",
    "content": "Build a SaaS product",
    "category": "idea",
    "tags": ["saas", "business"]
  }'

# Get memories
curl http://localhost:8001/api/memory/demo
```

## Database Schema

### Collections

**conversations** - Chat history with AI
```json
{
  "id": "uuid",
  "session_id": "string",
  "messages": [
    {
      "role": "user|assistant",
      "content": "string",
      "timestamp": "datetime"
    }
  ]
}
```

**memories** - Stored memories
```json
{
  "id": "uuid",
  "session_id": "string",
  "content": "string",
  "category": "idea|goal|project|note",
  "tags": ["string"],
  "created_at": "datetime"
}
```

**startups** - Startup simulations
```json
{
  "id": "uuid",
  "session_id": "string",
  "name": "string",
  "description": "string",
  "stage": "idea|mvp|launch|growth|scale",
  "metrics": {
    "users": 0,
    "revenue": 0.0,
    "funding": 0.0,
    "team_size": 1
  },
  "milestones": []
}
```

**designs** - Generated designs
```json
{
  "id": "uuid",
  "session_id": "string",
  "title": "string",
  "prompt": "string",
  "image_url": "string",
  "design_type": "slide|mockup|visual|logo"
}
```

## Features in Detail

### 1. Conversational AI
- Context-aware conversations
- Memory of previous interactions
- Intelligent brainstorming assistance
- Actionable insights and suggestions

### 2. Persistent Memory
- Store ideas, goals, and projects
- Categorize and tag memories
- Search across all memories
- Never lose important context

### 3. Startup Simulator
- Create startup profiles
- Simulate realistic growth
- Track metrics (users, revenue, funding)
- Generate milestone projections

### 4. Canvas Designer
- AI-powered image generation
- Multiple design types (slides, mockups, logos)
- Professional quality outputs
- Instant visual creation

## Error Handling

All endpoints return appropriate HTTP status codes:
- `200` - Success
- `404` - Not found
- `500` - Server error

Error response format:
```json
{
  "detail": "Error message"
}
```

## Development

### Running Tests
```bash
pytest tests/
```

### Code Quality
```bash
# Format code
black .

# Lint
flake8 .

# Type checking
mypy .
```

## Deployment

### Docker
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8001"]
```

### Environment Variables (Production)
- Set strong MongoDB credentials
- Use managed MongoDB service
- Configure proper CORS origins
- Enable rate limiting
- Add API key authentication

## Performance Tips

1. **Caching**: Implement Redis for frequently accessed data
2. **Connection Pooling**: Use MongoDB connection pooling
3. **Async Operations**: All database operations are async
4. **Rate Limiting**: Add rate limiting middleware
5. **Monitoring**: Use APM tools for performance tracking

## Security Considerations

- [ ] Implement API authentication
- [ ] Add rate limiting
- [ ] Validate all inputs
- [ ] Sanitize user content
- [ ] Use HTTPS in production
- [ ] Secure MongoDB with authentication
- [ ] Implement request logging
- [ ] Add CORS restrictions

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Add tests
5. Submit pull request

## License

MIT License

## Support

For issues and questions:
- Check API Documentation
- Review error logs
- Test with curl commands
- Verify MongoDB connection

---

Built with ❤️ for Emergent++

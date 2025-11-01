# EmergentX: The AI Co-Founder Workspace

EmergentX is an agentic AI ecosystem that simulates an entire startup team inside your browser. Users interact with a team of intelligent agents—a CEO, Engineer, Designer, and Marketer—that collaborate in real-time to turn a single prompt into a fully realized startup concept, complete with a strategy and brand identity.

## Project Structure

The project is a monorepo containing both the frontend and backend applications.

-   `/app`: The Next.js frontend application, creating the user interface.
-   `/components`: Shared React components for the frontend.
-   `/public`: Static assets like images and videos for the frontend.
-   `/backend`: A Python FastAPI server that powers the multi-agent AI logic.
    -   `/backend/services`: Contains all the core services for AI, memory, and agent orchestration.

## How It Works & API Key Integration

The backend powers a multi-agent pipeline where each AI agent (CEO, Engineer, etc.) has a unique personality and persistent memory. When a user sends a prompt, it's routed through this pipeline, with each agent building upon the previous one's work.

This entire system relies on the OpenAI API. To run the application, you must provide an API key.

### Environment Setup (`.env` file)

1.  Navigate to the `/backend` directory.
2.  Create a file named `.env`.
3.  Add your OpenAI API key to this file as follows:

```
OPENAI_API_KEY=sk-YourSecretApiKeyHere
```

The application uses the `openai` library to make calls to GPT-4o. It does not use LangChain. The key in your `.env` file is all that's needed to power the AI features.

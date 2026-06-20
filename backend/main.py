import os

from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("MODEL", "llama3")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "Tessa")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from orchestrator.graph import graph
from agents.policy_agent import policy_agent
from memory.state_manager import get_conversation_state

app = FastAPI()


# ENABLE CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# HOME ROUTE
@app.get("/")
def home():

    return {
        "message": "TechValleyMind Enterprise AI Running"
    }


# REQUEST MODEL
class ChatRequest(BaseModel):

    message: str

    session_id: str | None = None


# CHAT ROUTE
@app.post("/chat")
def chat(request: ChatRequest):

    session_id = request.session_id or "default_session"

    # POLICY VALIDATION
    policy_result = policy_agent(
        request.message
    )

    if policy_result["blocked"]:

        return {
            "response": policy_result["response"]
        }

    # GRAPH EXECUTION
    result = graph.invoke({

        "query": request.message,

        "session_id": session_id,

        "conversation_state": get_conversation_state(session_id)

    })

    return {

        "response": result["response"]

    }
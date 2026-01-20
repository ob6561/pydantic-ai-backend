from dotenv import load_dotenv
load_dotenv()  # MUST be first

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from agent import agent  # now safe to import


app = FastAPI(
    title="Pydantic AI Agent App",
    description="Full-stack generative AI agent using PydanticAI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200","https://genai-agent-ui.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TaskRequest(BaseModel):
    task: str


@app.post("/plan")
async def generate_plan(request: TaskRequest):
    result = await agent.run(request.task)
    try:
        return json.loads(result.output)
    except json.JSONDecodeError:
        # fallback for debugging
        return {"error": "Invalid JSON from agent", "raw": result.output}

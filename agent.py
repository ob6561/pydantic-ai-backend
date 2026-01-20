from pydantic_ai import Agent
from models import TaskPlan

agent = Agent[TaskPlan](
    model="groq:llama-3.1-8b-instant",
    system_prompt=(
        "You are a STRICT JSON generator.\n"
        "You MUST return ONLY valid JSON.\n"
        "Do NOT use markdown.\n"
        "Do NOT include explanations or extra text.\n"
        "The JSON MUST match this schema EXACTLY:\n"
        "{\n"
        '  "title": string,\n'
        '  "steps": string[],\n'
        '  "estimated_time": string\n'
        "}\n"
        "If you cannot comply, return valid JSON anyway."
    ),
)

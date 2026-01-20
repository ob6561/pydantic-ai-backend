from pydantic import BaseModel
from typing import List

class TaskPlan(BaseModel):
    title: str
    steps: List[str]
    estimated_time: str

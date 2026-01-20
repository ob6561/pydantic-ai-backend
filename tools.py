def estimate_time(task: str) -> str:
    """
    Simple heuristic-based tool to estimate task duration.
    Used by the AI agent.
    """
    task = task.lower()

    if "study" in task or "learn" in task:
        return "2 weeks"
    if "project" in task or "build" in task:
        return "1 week"
    if "resume" in task:
        return "2–3 days"

    return "Few days"

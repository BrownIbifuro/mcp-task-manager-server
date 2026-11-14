
from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import count

from mcp.server import MCPServer


# 1. Create the MCP server
mcp = MCPServer("Task Manager")


# 2. Define the structure of a task
@dataclass
class Task:
    id: int
    title: str
    completed: bool
    created_at: str


# 3. Store tasks in memory
tasks: list[Task] = []
task_id_counter = count(1)


# 4. Register our first MCP tool
@mcp.tool()
def create_task(title: str) -> dict:
    """Create a new task using the supplied title."""

    if not title.strip():
        raise ValueError("Task title cannot be empty.")

    task = Task(
        id=next(task_id_counter),
        title=title.strip(),
        completed=False,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

    tasks.append(task)

    return {
        "success": True,
        "message": "Task created successfully.",
        "task": {
            "id": task.id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at,
        },
    }

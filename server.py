
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from itertools import count

from mcp.server import MCPServer


# Create the MCP server
mcp = MCPServer("Task Manager")


# Define the structure of a task
@dataclass
class Task:
    id: int
    title: str
    completed: bool
    created_at: str


# In-memory task storage
tasks: list[Task] = []
task_id_counter = count(1)


# Tool 1: Create a task
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
        "task": asdict(task),
    }


# Tool 2: List all tasks
@mcp.tool()
def list_tasks() -> list[dict]:
    """Retrieve all tasks stored in the task manager."""

    return [asdict(task) for task in tasks]


# Tool 3: Complete a task
@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark a task as completed using its ID."""

    for task in tasks:
        if task.id == task_id:
            if task.completed:
                return {
                    "success": True,
                    "message": "Task is already completed.",
                    "task": asdict(task),
                }

            task.completed = True

            return {
                "success": True,
                "message": "Task completed successfully.",
                "task": asdict(task),
            }

    raise ValueError(f"Task with ID {task_id} was not found.")


# MCP Task Manager Server

A lightweight Python-based **Model Context Protocol (MCP) server** that exposes task-management functionality to compatible AI applications through three tools: creating tasks, retrieving tasks, and marking tasks as completed.

This project explores how MCP servers make application functionality available to AI assistants through structured, callable tools.

## Project Overview

The MCP Task Manager Server provides a simple task-management interface that an MCP-compatible client can use to interact with task data.

Instead of requiring an AI application to understand the internal implementation of a task manager, the server exposes clearly defined tools that clients can discover and invoke.

### Features

- **Create tasks:** Add tasks with automatically generated IDs and UTC timestamps.
- **List tasks:** Retrieve all tasks currently stored by the server.
- **Complete tasks:** Mark an existing task as completed using its ID.
- **Input validation:** Reject empty or whitespace-only task titles.
- **Error handling:** Return appropriate errors when a task ID cannot be found.
- **Completion checks:** Identify tasks that have already been completed.

## Technology Stack

- Python
- Model Context Protocol (MCP)
- MCP Python SDK
- pytest

## Project Structure

```text
mcp-task-manager-server/
│
├── server.py
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── README.md
│
└── tests/
    └── test_server.py
```

## Getting Started

### Prerequisites

- Python 3.14.6 (version used during development and testing)
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/BrownIbifuro/mcp-task-manager-server.git
```

Navigate into the project directory:

```bash
cd mcp-task-manager-server
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Install development dependencies, including pytest:

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Launch the MCP development environment

Run:

```bash
mcp dev server.py
```

This launches the MCP development environment and allows you to inspect and interact with the server's tools.

## Available MCP Tools

The server exposes three tools.

| Tool | Description |
|---|---|
| `create_task` | Creates a task using a supplied title. |
| `list_tasks` | Retrieves all stored tasks. |
| `complete_task` | Marks a task as completed using its ID. |

For detailed input parameters, responses, and error behaviour, see the tool reference documentation.

## Running the Tests

Run the test suite from the project root:

```bash
python -m pytest -v
```

The current test suite contains eight tests covering:

- Successful task creation.
- Whitespace trimming.
- Empty-title validation.
- Retrieving existing tasks.
- Retrieving an empty task list.
- Successful task completion.
- Completing an already completed task.
- Handling unknown task IDs.

**Latest recorded test result:** 8 passed.

## Current Limitations

This project is an early-stage implementation with the following limitations:

- **In-memory storage:** Tasks are stored in a Python list and are not persisted to a database or file.
- **Server restarts:** All stored tasks are lost when the server process restarts.
- **Single-process storage:** The implementation does not provide shared storage across multiple server instances.
- **Limited operations:** The current implementation supports creating, listing, and completing tasks. Editing and deleting tasks are not implemented.

## Future Improvements

Potential areas for further development include:

- Persistent task storage using SQLite or another database.
- Task editing and deletion.
- Additional filtering and task-status queries.
- More comprehensive integration testing.
- Improved support for deployment and configuration.

## Learning Objectives

This project was built to explore:

- The structure of a Python MCP server.
- How MCP tools expose application functionality.
- How tool inputs and outputs are defined.
- Input validation and error handling.
- Testing server functionality with pytest.
- Inspecting and testing MCP tools through the MCP development environment.

## Author

**Ibifuro Brown Sunday**

- GitHub: [BrownIbifuro](https://github.com/BrownIbifuro)
- LinkedIn: [Ibifuro Brown](https://linkedin.com/in/ibifuro-brown-15512b225/)
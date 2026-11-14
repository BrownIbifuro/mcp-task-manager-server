# Installation and Setup Guide

This guide explains how to install, configure, and run the MCP Task Manager Server locally.

It covers the prerequisites, repository setup, dependency installation, launching the MCP development environment, and running the automated tests.

## 1. Prerequisites

Before getting started, ensure you have the following installed:

| Requirement | Description |
|---|---|
| Python | Python 3.14.6 was used during project development and testing. |
| pip | Python package installer. |
| Git | Required to clone the repository. |
| Terminal | PowerShell on Windows, or a terminal on macOS/Linux. |

The project dependencies specify MCP Python SDK version 2, with the CLI extra enabled.

## 2. Clone the Repository

Open your terminal and clone the project:

```bash
git clone https://github.com/BrownIbifuro/mcp-task-manager-server.git
```

Move into the project directory:

```bash
cd mcp-task-manager-server
```

## 3. Create a Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python projects on your computer.

Create one using:

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Once activated, your terminal prompt should display `(.venv)`.

## 4. Install Project Dependencies

The repository contains two dependency files.

### Main dependencies

Install the application dependencies:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
mcp[cli]>=2,<3
```

This installs the MCP Python SDK with its CLI extras, allowing the project to use the MCP development command.

### Development dependencies

To install the testing dependencies, run:

```bash
python -m pip install -r requirements-dev.txt
```

The `requirements-dev.txt` file contains:

```text
-r requirements.txt
pytest>=8
```

The `-r requirements.txt` directive includes the main application dependencies, while `pytest>=8` installs pytest for automated testing.

## 5. Verify the Installation

Check that Python is available:

```bash
python --version
```

Check the installed MCP package:

```bash
python -m pip show mcp
```

Check pytest:

```bash
python -m pytest --version
```

These commands help confirm that the environment has the expected tools installed.

## 6. Launch the MCP Development Environment

From the project root, with the virtual environment activated, run:

```bash
mcp dev server.py
```

This launches the MCP development environment and provides an interface for inspecting and interacting with the server.

Use the interface to test the three available tools:

- `create_task`
- `list_tasks`
- `complete_task`

For example, create a task with the title `Read MCP documentation`, then retrieve the task list to inspect the result.

**Note:** The development environment is intended for local inspection and testing. It is not a production deployment configuration.

## 7. Run the Automated Tests

The project uses pytest to test its task-management functionality.

Run the tests from the project root:

```bash
python -m pytest -v
```

The current test suite covers:

| Test area | Expected behaviour |
|---|---|
| Task creation | A valid task is created successfully. |
| Input validation | Empty titles are rejected. |
| Whitespace handling | Leading and trailing whitespace is removed. |
| Task retrieval | Stored tasks are returned. |
| Empty task list | An empty list is returned when no tasks exist. |
| Task completion | An existing task is marked completed. |
| Repeated completion | An already completed task is handled successfully. |
| Invalid task ID | An error is raised when the requested task does not exist. |

The latest recorded test run completed with **8 passing tests**.

## 8. Important Storage Behaviour

The server currently stores tasks in an in-memory Python list.

This means:

- Tasks remain available while the server process is running.
- Tasks are not saved to a database or file.
- Restarting the server clears the stored tasks.
- The current implementation does not provide persistent storage across server instances.

This is an intentional limitation of the current implementation, not an installation error.

## 9. Deactivate the Virtual Environment

When you finish working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

You can activate it again the next time you work on the project.

## 10. Next Steps

After completing installation:

1. Launch the MCP development environment.
2. Inspect the available tools.
3. Create and retrieve a task.
4. Mark a task as completed.
5. Run the automated test suite.

For details about the available tools, their parameters, responses, and error handling, see the [Tool Reference](tools-reference.md).
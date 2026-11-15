# Troubleshooting Guide

This guide covers common setup, installation, testing, and runtime issues you may encounter when working with the MCP Task Manager Server.

## 1. The `mcp` command is not recognized

**Possible error:**

```text
'mcp' is not recognized as the name of a cmdlet, function, script file, or executable program.
```

**Cause:**

The project's virtual environment may not be activated, or the MCP package may not be installed in the active environment.

**Solution:**

1. Navigate to the project directory.
2. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the project dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Try starting the development environment again:

   ```powershell
   mcp dev server.py
   ```

## 2. The MCP package cannot be imported

**Possible error:**

```text
ModuleNotFoundError: No module named 'mcp'
```

**Cause:**

The MCP package may not be installed in the Python environment currently being used.

**Solution:**

Activate the project's virtual environment and install the dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Verify the installation:

```powershell
pip show mcp
```

## 3. Pytest cannot find the server module

**Observed issue:**

Running the test suite directly with:

```powershell
pytest -v
```

previously resulted in:

```text
ModuleNotFoundError: No module named 'server'
```

**Solution:**

Run pytest through Python instead:

```powershell
python -m pytest -v
```

This invokes pytest as a Python module using the active interpreter.

## 4. Tasks disappear after restarting the server

**Cause:**

The application currently stores tasks in an in-memory Python list:

```python
tasks: list[Task] = []
```

This means task data exists only while the server process is running.

**Solution:**

There is currently no persistence mechanism in this version of the project. Tasks will need to be created again after restarting the server.

A future improvement would be to introduce persistent storage using SQLite or another database.

## 5. A task title is rejected

**Possible error:**

```text
ValueError: Task title cannot be empty.
```

**Cause:**

The `create_task` tool does not accept empty titles or strings containing only whitespace.

**Solution:**

Provide a title containing at least one non-whitespace character.

For example:

```text
Prepare project documentation
```

## 6. A task cannot be completed

**Possible error:**

```text
ValueError: Task with ID 10 was not found.
```

**Cause:**

The supplied task ID does not match an existing task.

**Solution:**

1. Call `list_tasks` to retrieve the available tasks.
2. Identify the ID of the task you want to complete.
3. Pass that ID to `complete_task`.

Remember that task IDs restart from 1 when the server process restarts because tasks are stored in memory.

## 7. Running the MCP development environment

To launch the development environment, activate the virtual environment and run:

```powershell
mcp dev server.py
```

If the development environment does not launch, check that:

- You are in the project root directory.
- The virtual environment is active.
- The project dependencies have been installed.
- The `server.py` file exists in the current directory.

## Getting Further Help

If you encounter an issue not covered in this guide:

1. Check the error message carefully.
2. Confirm that you are using the project's virtual environment.
3. Review the [Installation Guide](installation.md).
4. Review the [Tool Reference](tools-reference.md) to understand tool inputs, outputs, and error behaviour.

## Known Project Limitations

This version of the MCP Task Manager Server:

- Stores tasks in memory rather than a database.
- Does not support editing or deleting tasks.
- Resets task data when the server restarts.
- Does not provide user authentication or multi-user task management.

These are current implementation limitations, not installation errors.
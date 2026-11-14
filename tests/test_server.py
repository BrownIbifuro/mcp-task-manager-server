
from itertools import count

import pytest

import server


@pytest.fixture(autouse=True)
def reset_task_storage(monkeypatch):
    """Give every test a clean task store and ID counter."""
    monkeypatch.setattr(server, "tasks", [])
    monkeypatch.setattr(server, "task_id_counter", count(1))


def test_create_task_successfully():
    result = server.create_task("Read MCP documentation")

    assert result["success"] is True
    assert result["task"]["id"] == 1
    assert result["task"]["title"] == "Read MCP documentation"
    assert result["task"]["completed"] is False
    assert result["task"]["created_at"]


def test_create_task_trims_whitespace():
    result = server.create_task("  Learn Python  ")

    assert result["task"]["title"] == "Learn Python"


def test_create_task_rejects_empty_title():
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        server.create_task("   ")


def test_list_tasks_returns_all_tasks():
    server.create_task("Task one")
    server.create_task("Task two")

    result = server.list_tasks()

    assert len(result) == 2
    assert result[0]["title"] == "Task one"
    assert result[1]["title"] == "Task two"


def test_list_tasks_returns_empty_list():
    assert server.list_tasks() == []


def test_complete_task_successfully():
    created = server.create_task("Finish tutorial")
    task_id = created["task"]["id"]

    result = server.complete_task(task_id)

    assert result["success"] is True
    assert result["task"]["completed"] is True
    assert result["message"] == "Task completed successfully."


def test_complete_task_that_is_already_completed():
    created = server.create_task("Finish tutorial")
    task_id = created["task"]["id"]

    server.complete_task(task_id)
    result = server.complete_task(task_id)

    assert result["success"] is True
    assert result["task"]["completed"] is True
    assert result["message"] == "Task is already completed."


def test_complete_task_with_unknown_id():
    with pytest.raises(ValueError, match="Task with ID 999 was not found"):
        server.complete_task(999)

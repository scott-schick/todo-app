"""
storage.py

Handles saving and loading the to-do list to/from a JSON file,
so tasks aren't lost when the program closes.
"""

import json
import os

from todo import Todo

DEFAULT_FILE = os.path.join("data", "tasks.json")


def save_tasks(tasks, filename=DEFAULT_FILE):
    """Save a list of Todo objects to a JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)


def load_tasks(filename=DEFAULT_FILE):
    """Load a list of Todo objects from a JSON file.

    Returns an empty list if the file doesn't exist yet.
    """
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as f:
        data = json.load(f)

    return [Todo.from_dict(item) for item in data]

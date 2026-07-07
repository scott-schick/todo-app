"""
todo.py

Defines the Todo class: a single to-do item.
This keeps the "what is a task?" logic separate from
the "how do we store/show tasks?" logic in other files.
"""


class Todo:
    def __init__(self, text, done=False):
        self.text = text
        self.done = done

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

    def to_dict(self):
        """Convert this Todo into a plain dictionary (for saving to a file)."""
        return {"text": self.text, "done": self.done}

    @staticmethod
    def from_dict(data):
        """Create a Todo object from a dictionary (for loading from a file)."""
        return Todo(text=data["text"], done=data["done"])

    def __str__(self):
        checkbox = "[x]" if self.done else "[ ]"
        return f"{checkbox} {self.text}"

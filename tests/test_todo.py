"""
test_todo.py

A few simple tests for the Todo class.
Run with:

    python -m unittest discover tests
"""

import sys
import os
import unittest

# Allow importing todo.py from the parent folder
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from todo import Todo


class TestTodo(unittest.TestCase):
    def test_new_task_is_not_done(self):
        task = Todo("Learn git")
        self.assertFalse(task.done)

    def test_mark_done(self):
        task = Todo("Learn git")
        task.mark_done()
        self.assertTrue(task.done)

    def test_mark_undone(self):
        task = Todo("Learn git", done=True)
        task.mark_undone()
        self.assertFalse(task.done)

    def test_to_dict_and_back(self):
        task = Todo("Learn git", done=True)
        data = task.to_dict()
        rebuilt = Todo.from_dict(data)

        self.assertEqual(task.text, rebuilt.text)
        self.assertEqual(task.done, rebuilt.done)

    def test_string_format(self):
        done_task = Todo("Learn git", done=True)
        not_done_task = Todo("Learn GitHub", done=False)

        self.assertEqual(str(done_task), "[x] Learn git")
        self.assertEqual(str(not_done_task), "[ ] Learn GitHub")


if __name__ == "__main__":
    unittest.main()

# To-Do List App

A tiny command-line to-do list, built for learning **Python** and **Git**. Designed for Camp Integem, Irvine 2026.

This project is intentionally simple. It's meant to be a sandbox for practicing
git commands like `clone`, `add`, `commit`, `branch`, `merge`, and `push` —
not a showcase of advanced Python.

## Features

- Add tasks
- View tasks
- Mark tasks as done
- Remove tasks
- Tasks are saved automatically to `data/tasks.json`

## Project structure

```
todo-app/
├── main.py           # Entry point — run this file to start the app
├── todo.py           # The Todo class (what a task looks like)
├── storage.py         # Saving and loading tasks from a file
├── tests/
│   └── test_todo.py  # Simple automated tests
├── data/              # Saved tasks show up here (ignored by git)
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Getting started

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd todo-app
   ```

2. Run the app (requires Python 3.8+, no extra installs needed):

   ```bash
   python main.py
   ```

3. Run the tests:

   ```bash
   python -m unittest discover tests
   ```

## Ideas for practicing git with this project

Great first exercises for a class:

- Create a new branch and add a "priority" field to tasks.
- Fix a bug on a branch, then open a pull request.
- Have two people each edit `main.py` differently and practice resolving a
  merge conflict.
- Add a new feature (like editing a task's text) and write a test for it.
- Use `git log` and `git blame` to see who changed what, and when.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

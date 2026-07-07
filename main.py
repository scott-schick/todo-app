"""
main.py

The entry point for the To-Do List app.
Run this file to start the program:

    python main.py
"""

from todo import Todo
from storage import load_tasks, save_tasks

MENU = """
==== TO-DO LIST ====
1. View tasks
2. Add task
3. Mark task as done
4. Remove task
5. Quit
"""


def print_tasks(tasks):
    if not tasks:
        print("\nYour list is empty. Add a task with option 2!")
        return

    print()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task(tasks):
    text = input("What do you need to do? ").strip()
    if text:
        tasks.append(Todo(text))
        print(f'Added: "{text}"')
    else:
        print("Task cannot be empty.")


def complete_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    choice = input("Which task number is done? ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        tasks[int(choice) - 1].mark_done()
        print("Nice work! Task marked as done.")
    else:
        print("That's not a valid task number.")


def remove_task(tasks):
    print_tasks(tasks)
    if not tasks:
        return

    choice = input("Which task number should be removed? ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        removed = tasks.pop(int(choice) - 1)
        print(f'Removed: "{removed.text}"')
    else:
        print("That's not a valid task number.")


def main():
    tasks = load_tasks()

    while True:
        print(MENU)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")

        save_tasks(tasks)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""A simple command-line to-do list manager."""

import argparse
import json
from pathlib import Path

TODO_FILE = Path.home() / ".todo.json"


def load_tasks(path=TODO_FILE):
    """Read tasks from disk. Returns an empty list if the file doesn't exist."""
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks, path=TODO_FILE):
    """Write tasks to disk as JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks, text):
    """Add a new task to the list."""
    tasks.append({"text": text, "done": False})
    return tasks


def complete_task(tasks, number):
    """Mark task number `number` (1-based) as done."""
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task with number {number}")
    tasks[number - 1]["done"] = True
    return tasks


def remove_task(tasks, number):
    """Delete task number `number` (1-based)."""
    if not 1 <= number <= len(tasks):
        raise IndexError(f"No task with number {number}")
    tasks.pop(number - 1)
    return tasks


def format_tasks(tasks):
    """Turn the task list into a printable string."""
    if not tasks:
        return "No tasks yet. Add one with: todo add \"buy milk\""
    lines = []
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{i}. [{mark}] {task['text']}")
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description="A simple to-do list manager.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("text", help="what you need to do")

    sub.add_parser("list", help="show all tasks")

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("number", type=int, help="task number")

    p_remove = sub.add_parser("remove", help="delete a task")
    p_remove.add_argument("number", type=int, help="task number")

    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    tasks = load_tasks()

    try:
        if args.command == "add":
            add_task(tasks, args.text)
            print(f"Added: {args.text}")
        elif args.command == "done":
            complete_task(tasks, args.number)
            print(f"Completed task {args.number}")
        elif args.command == "remove":
            remove_task(tasks, args.number)
            print(f"Removed task {args.number}")
        elif args.command == "list":
            print(format_tasks(tasks))
            return
    except IndexError as err:
        print(f"Error: {err}")
        return

    save_tasks(tasks)


if __name__ == "__main__":
    main()

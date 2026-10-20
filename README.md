# todo-cli

A simple command-line to-do list manager written in Python. No dependencies needed.

## Usage

```bash
python todo.py add "buy milk"
python todo.py add "finish homework"
python todo.py list
python todo.py done 1
python todo.py remove 2
```

Example output:

```
1. [x] buy milk
2. [ ] finish homework
```

Tasks are saved in `~/.todo.json`.

## Requirements

Python 3.8 or newer.

## Running the tests

```bash
pip install pytest
pytest
```

## Ideas for extending it

- Add due dates or priorities
- Add an `edit` command
- Add colors to the output
- Add a `clear` command to remove all completed tasks

## License

MIT

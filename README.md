# Task Tracker CLI

A simple command-line application to manage your tasks efficiently.

## Features

* Add tasks
* Update tasks
* Delete tasks
* Mark tasks as in-progress or done
* List tasks (all / filtered by status)
* Storage using JSON

## Tech Stack
* Python
* JSON file handling
* CLI using sys.argv

## Installation
git clone https://github.com/fluxx-07/todo-cli.git

cd todo-cli

## Usage

### Add a task

python todo.py add "Buy groceries"

### List tasks

python todo.py list

### List by status

python todo.py list done
python todo.py list todo
python todo.py list in-progress

### Update task

python todo.py update 1 "Buy milk and bread"

### Delete task

python todo.py delete 1

### Mark task

python todo.py mark-in-progress 1
python todo.py mark-done 1

# 0x00. AirBnB clone - The console

## Group project

- **Language:** Python
- **Concepts:** OOP

### By: Guillaume
- **Weight:** 5
- **Team:** Mark Ongaro, Nessy Mputhia

### Project Details
- **Start:** Feb 5, 2024 6:00 AM
- **End:** Feb 12, 2024 6:00 AM
- **Checker Release:** Feb 10, 2024 12:00 PM
- **Manual QA Review:** Required
- **Auto Review:** Launched at the deadline

## Concepts
For this project, we expect you to look at these concepts:
- Python packages
- AirBnB clone

## Background Context
Welcome to the AirBnB clone project! Before starting, please read the AirBnB concept page.

### First step
Write a command interpreter to manage your AirBnB objects. This is the first step towards building your first full web application: the AirBnB clone. Each task is linked and will help you to:
- Put in place a parent class (called BaseModel) to take care of the initialization, serialization, and deserialization of your future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
It's similar to the Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database, etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources
Read or watch:
- [cmd module](https://docs.python.org/3/library/cmd.html)
- [cmd module in depth](https://docs.python.org/3/library/cmd.html#cmd.Cmd)
- [Python packages concept page](https://docs.python.org/3/tutorial/modules.html)
- [uuid module](https://docs.python.org/3/library/uuid.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [args/kwargs](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
- [Python test cheatsheet](https://github.com/mattharrison/PythonTestCheatSheet)
- [cmd module wiki page](https://en.wikipedia.org/wiki/Cmd_(command))

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks yourself to meet the learning objectives.
- Plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### Python Scripts
- **Allowed editors:** vi, vim, emacs
- **Interpreted/compiled:** Ubuntu 20.04 LTS using python3 (version 3.8.5)
- **File endings:** Should end with a new line
- **First line:** Should be `#!/usr/bin/python3`
- **README.md:** Mandatory at the root of the folder
- **Coding style:** Should use pycodestyle (version 2.8.*)
- **Executable:** All files must be executable
- **Documentation:** All modules, classes, and functions should have documentation

### Python Unit Tests
- **Editors:** vi, vim, emacs
- **File endings:** Should end with a new line
- **Folders:** All test files should be inside a folder `tests`
- **Module:** Should use the unittest module
- **File extensions:** All test files should have the extension `.py`
- **Naming convention:** Test files and folders should start with `test_`
- **File organization:** Should mirror your project structure
- **Documentation:** All modules, classes, and functions should have documentation
- **Collaboration:** Working together on test cases is encouraged

## GitHub
- There should be one project repository per group.
- Cloning/forking a project repository with the same name before the second deadline risks a 0% score.

## Execution
Your shell should work like this in interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$


$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

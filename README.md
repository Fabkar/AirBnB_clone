<p align="center">
  <img src="https://i.imgur.com/ogbfW3k.png">
</p>

<h1 align="center">AirBnB_Clone</h1>


## BACKGROUND
This is a colaboration project between two software development students at [Holberton School](https://www.holbertonschool.com/) from Cohort 12, this project is about create an AirBnB clone, where we'll applied different concepts learned about python starting by write a command interpreter to manage our AirBnB objects.

## AirBnB Clone
Airbnb clone is a command interpetrer to manage and we will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration among others.

## Features
Airbnb is a complex platform that combines severals features. In this clone we have differents classes and each those classes has possibility to update and deletes it self.

    -- Create a new object (ex: a new User or a new Place)
    -- Retrieve an object from a file, a database etc…
    -- Do operations on objects (count, compute stats, etc…)
    -- Update attributes of an object
    -- Destroy an object

## Class:
  - User
  - City
  - Place
  - Review
  - State
  - Amenity

---
## Installation
In this seasson we show how isntall step by step the interpreter, it's very simple.
Following the next steps
  - Copy this line in your terminal `git clone https://github.com/1uiscalderon/AirBnB_clone`
  - if you dont have permission, you should use `chmod u+x <on file console.py>`
  - To execute the console, you'll need use `./console.py`

---
## Manual about Interpreter - How to use  
| Command | Description |
|:-------:|:-----------:|
|help     | list all commands of console|
|EOF      | End of file   |
|all      | Print all elements of storage as a string|
|count    | Show the number of instance inside the storage of file json|
|Create   | Create a new instance from base model| 
|Destroy  | Deletes an instance based on the class name and id|
|quit     | Command to exit the program|
|show     | Representation of an instance based on the class name and id|
|update   | Updates an instance based on the class name and id by adding or updating attribute|

---

## Techstack

<p align="center">
  <img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T192548Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2d8a53671aae3823e317f8574d4c786856059f805600f1558078ee4a14d9aec5">
</p>

## Usage

- All files are interpreted/compiled on Ubuntu 14.04 LTS using Python3 (version 3.4.3)
- All code use the PEP 8 style (version 1.7.0.\*)
- The console works in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

The console also works in non-interactive mode:

```sh
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
```

## Testing

- All unittests can be executed with:

```
python3 -m unittest discover tests
```

---

### Requirements and modules to development - Resources
  - [cmd module](https://docs.python.org/3.4/library/cmd.html)
  - packages concept page
  - [uuid module](https://docs.python.org/3.4/library/uuid.html)
  - [datetime](https://docs.python.org/3.4/library/datetime.html)
  - [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  - [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
  - [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)


## AUTHORS

- [**Fabian Andres Carmona Vargas**] (https://github.com/Fabkar)
- [**Luis MIguel Calderon Escobar**] (https://github.com/1uiscalderon)


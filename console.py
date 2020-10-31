#!/usr/bin/python3
"""
Function speccify a Console the entry point of the command interpreter
"""
from models import storage
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Define the class HBNB as interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit Success
        """
        return True

    def emptyline(self):
        """
        when recive an empty line do nothing.
        """
        pass

    def do_create(self, line):
        """
        create a new instance from base model
        """
        if len(line) == 0:
            print("** class name missing **")
            return False
        try:
            split_line = shlex.split(line)
            _instance = eval(split_line[0])()
            _instance.save()
            print(_instance.id)

        except Exception:
            print("** class doesn't exist **")
            return False

    def do_show(self, line):
        """
        Representation of an instance based on the class name and id
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        if len(split_line) < 2:
            print("** instance id missing **")
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False

        tmp_key = split_line[0] + "." + split_line[1]
        if tmp_key in storage.all().keys():
            del(storage.all()[tmp_key])
            storage.save()
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Method to Deletes an instance based on the class name and id.
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        if len(split_line) < 2:
            print("** instance id missing **")
            return False

        tmp_key = split_line[0] + "." + split_line[1]
        if tmp_key in storage.all().keys():
            del(storage.all()[tmp_key])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Method to print all elements of storage as a list of string
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print([str(v) for v in storage.all().values()])
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        print([str(v) for k, v in storage.all().items()
              if split_line[0] in k])

    def do_update(self, line):
        """
        Method to Updates an instance based on the class name
        and id by adding or updating attribute
        """
        split_line = shlex.split(line)
        if len(split_line) == 0:
            print("** class name missing **")
            return False
        try:
            eval(split_line[0])
        except Exception:
            print("** class doesn't exist **")
            return False
        if len(split_line) < 2:
            print("** instance id missing **")
        elif split_line[0] + "." + split_line[1] not in storage.all().keys():
            print("** no instance found **")
        elif len(split_line) < 3:
            print("** attribute name missing **")
        elif len(split_line) < 4:
            print("** value missing **")
        else:
            tmp_key = split_line[0] + "." + split_line[1]
            if split_line[3][0] == "\"":
                split_line[3] = split_line[3][1: -1] 
            setattr(storage.all()[tmp_key],split_line[2],split_line[3])
            storage.all()[tmp_key].save()
            print("hey")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

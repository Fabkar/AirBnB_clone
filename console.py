#!/usr/bin/python3
"""
Function speccify a Console the entry point of the command interpreter
"""
import cmd


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
        """
        Exit Success
        """
        return True

    def emptyline(self):
        """
        when recive an empty line do nothing.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/python3


"""
    Module that defines HBNBCommand class
    which is a child class of Cmd class
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ A representation of HBNBCommand class """
    prompt = "(hbnh) "

    # ----- basic HBnB commands -----
    def emptyline(self):
        pass

    def do_EOF(self, args):
        """ EOF command to exit the program """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

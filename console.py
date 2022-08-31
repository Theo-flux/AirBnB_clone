#!/usr/bin/python3


"""
    Module that defines HBNBCommand class
    which is a child class of Cmd class
"""


import cmd
from models.base_model import BaseModel


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
    
    def do_create(self, args):
        """ Creates a new instance of a class """
        if args:
            if args == "BaseModel":
                my_model = BaseModel()
                my_model.name = "Model created from console"
                my_model.my_number = 102
                my_model.save()
                print(my_model.id)
            else:
                print("** class name doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

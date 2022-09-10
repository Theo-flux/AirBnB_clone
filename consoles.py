#!/usr/bin/python3


"""
    Module that defines HBNBCommand class
    which is a child class of Cmd class
"""


import cmd
import json
import models
import re


storage = models.storage
BaseModel = models.base_model.BaseModel
User = models.user.User
State = models.state.State
Place = models.place.Place
City = models.city.City
Amenity = models.amenity.Amenity
Review = models.review.Review


def find_match(arg):
    pattern = '^[A-Za-z]*.?[a-z]+\\([\"0-9a-f-\"]*\\)$'
    result = re.findall(r'{}'.format(pattern), arg)
    return result


def split_match(arg):
    arg = list(arg[0].split("."))
    return arg


def find_inner_match(arg):
    pattern = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    result = re.findall(pattern, arg[1])
    return result


class HBNBCommand(cmd.Cmd):
    """ A representation of HBNBCommand class """
    prompt = "(hbnh) "
    __model_list = [
        "BaseModel",
        "User",
        "State",
        "Place",
        "Amenity",
        "City",
        "Review"
    ]
    __short_cut_command_dict = {
        "all()": "do_all",
        "create()": "do_create",
        "show()": "do_show",
        "destroy()": "do_destroy",
        "update()": "do_update",
        "count()": "count"
    }

    # ----- basic HBnB commands -----
    """
    def default(self, line):
        match = find_match(line)
        # print(match)
        if match:
            match = split_match(match)
            # print("--split--")
            # print(match)
            # print("----------")
            # print(find_inner_match(match))
            if len(match) > 1:

                try:
                    value = HBNBCommand.__short_cut_command_dict[match[1]]
                except KeyError:
                    print("** unknown command: {}".format(match[1]))
                else:
                    eval("self.{}('{}')".format(value, match[0]))

            elif len(match) == 1:
                try:
                    value = HBNBCommand.__short_cut_command_dict[match[0]]
                except KeyError:
                    print("** unknown command: {}".format(match[0]))
                else:
                    eval("self.{}()".format(value))
        else:
            print("** Unknown syntax: {}".format(line))
    """
    def emptyline(self):
        pass

    def do_EOF(self, args):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def create(self, args):
        """Creates a new instance of BaseModel\n
        (usage: create <classname>)\n
        """

        if args:
            if args in HBNBCommand.__model_list:
                newInstance = eval(args)()
                newInstance.save()
                print(newInstance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def show(self, args):
        """Prints the string representation of an instance\n
        based on the class name and id\n
        (usage: show <classname> <id>)\n
        """
        # key 0 conatins the classname key 1 contains the id
        show_dict = {"0": "", "1": ""}
        obj_dict = {}
        res = {}
        i = 0

        if args:
            args = list(args.split(" "))

            while i < len(args):
                show_dict[str(i)] = args[i]
                i += 1

            if show_dict["0"] in HBNBCommand.__model_list:
                if show_dict["1"]:
                    with open("file.json", mode="r") as fp:
                        obj_dict = json.load(fp)

                    for key, value in obj_dict.items():
                        if value["id"] == show_dict["1"]:
                            res = value

                    if res != {}:
                        res = eval(show_dict["0"])(**res)
                        print(res)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def destroy(self, args):
        """Deletes an instance based on the class name and id\n
        (usage: destroy <classname> <id>)\n
        """

        show_dict = {"0": "", "1": ""}
        obj_dict = {}
        dict_key = ""
        i = 0

        if args:
            args = list(args.split(" "))

            while i < len(args):
                show_dict[str(i)] = args[i]
                i += 1

            if show_dict["0"] in HBNBCommand.__model_list:
                if show_dict["1"]:
                    with open("file.json", mode="r") as fp:
                        obj_dict = json.load(fp)

                    for key, value in obj_dict.items():
                        if value["id"] == show_dict["1"]:
                            dict_key = key

                    if dict_key != "":
                        del obj_dict[dict_key]

                        with open("file.json", mode="w") as fp:
                            json.dump(obj_dict, fp)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def all(self, args=""):
        """Prints all string representation of all instances\n
        based or not on the class name.\n
        (usage: all BaseModel or all)\n
        """
        obj_dict = {}
        obj_dict_by_model = {}
        if args:
            if args in HBNBCommand.__model_list:
                with open("file.json", mode="r") as fp:
                    obj_dict = json.load(fp)

                for key, value in obj_dict.items():
                    if value["__class__"] == args:
                        res = eval(value["__class__"])(**value)
                        print(res)
            else:
                print("** class doesn't exist **")
        else:
            with open("file.json", mode="r") as fp:
                obj_dict = json.load(fp)

            for value in obj_dict.values():
                res = eval(value["__class__"])(**value)
                print(res)

    def count(self, args=""):
        """Counts number of instances of a class\n
        (usage: <class name>.count()\n
        """
        obj_dict = {}
        obj_dict_by_model = {}
        if args:
            if args in HBNBCommand.__model_list:
                with open("file.json", mode="r") as fp:
                    obj_dict = json.load(fp)

                for key, value in obj_dict.items():
                    if value["__class__"] == args:
                        obj_dict_by_model[key] = value
                print(len(obj_dict_by_model))

            else:
                print("** class doesn't exist **")
        else:
            with open("file.json", mode="r") as fp:
                obj_dict = json.load(fp)
            print(len(obj_dict))

    def update(self, args):
        """Update an instance based ob the class name and id\n
        by adding or updating attribute (usage: update <class name>\
        <id> <attribute name> "<attribute value>")\n
        """
        update_dict = {"0": "", "1": "", "2": "", "3": ""}
        obj_dict = {}
        dict_key = ""
        res = {}
        i = 0

        if args:
            args = list(args.split(" "))

            while i < len(args):
                update_dict[str(i)] = args[i]
                i += 1

            if update_dict["0"] in HBNBCommand.__model_list:
                if update_dict["1"]:
                    with open("file.json", mode="r") as fp:
                        obj_dict = json.load(fp)

                    for key, value in obj_dict.items():
                        if value["id"] == update_dict["1"]:
                            res = value

                    if res != {}:
                        if update_dict["2"]:
                            if update_dict["3"]:
                                for key, value in obj_dict.items():

                                    if value["id"] == update_dict["1"]:
                                        attr = update_dict["2"]
                                        value[attr] = update_dict["3"]
                                print(obj_dict)
                                with open("file.json", mode="w") as fp:
                                    json.dump(obj_dict, fp)
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

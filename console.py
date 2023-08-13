#!/usr/bin/python3
"""HolbertonBnB Console - Interactive Command Line Utility"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def custom_arg_parser(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HolbertonBnBCommand(cmd.Cmd):
    """HolbertonBnB Command Line Interface
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for the command when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Invalid syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a new instance of a class and print its ID.
        """
        argl = custom_arg_parser(arg)
        if len(argl) == 0:
            print("** Class name missing **")
        elif argl[0] not in HolbertonBnBCommand.__classes:
            print("** Class doesn't exist **")
        else:
            new_instance = eval(argl[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of a class instance with the given ID.
        """
        argl = custom_arg_parser(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** Class name missing **")
        elif argl[0] not in HolbertonBnBCommand.__classes:
            print("** Class doesn't exist **")
        elif len(argl) == 1:
            print("** Instance ID missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict:
            print("** No instance found **")
        else:
            print(obj_dict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance with the given ID."""
        argl = custom_arg_parser(arg)
        obj_dict = storage.all()
        if len(argl) == 0:
            print("** Class name missing **")
        elif argl[0] not in HolbertonBnBCommand.__classes:
            print("** Class doesn't exist **")
        elif len(argl) == 1:
            print("** Instance ID missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** No instance found **")
        else:
            del obj_dict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class>
        Display string representations of instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = custom_arg_parser(arg)
        if len(argl) > 0 and argl[0] not in HolbertonBnBCommand.__classes:
            print("** Class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(argl) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Usage: count <class>
        Retrieve the number of instances of a given class."""
        argl = custom_arg_parser(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value>
        Update a class instance's attribute with a given value."""
        argl = custom_arg_parser(arg)
        obj_dict = storage.all()

        if len(argl) == 0:
            print("** Class name missing **")
            return False
        if argl[0] not in HolbertonBnBCommand.__classes:
            print("** Class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** Instance ID missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in obj_dict.keys():
            print("** No instance found **")
            return False
        if len(argl) == 2:
            print("** Attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** Value missing **")
                return False

        if len(argl) == 4:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = val_type(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = obj_dict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argl[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)
                else:
                    obj.__dict__[key] = value
        storage.save()


if __name__ == "__main__":
    HolbertonBnBCommand().cmdloop()

#!/usr/bin/python3
import cmd
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models import storage
from models.review import Review
from datetime import datetime

"""
Module console.py - a command-line interface for Holberton AirBnB
"""

class HBNBCommand(cmd.Cmd):
    ''' Holberton AirBnB command interpreter class '''
    prompt = "(hbnb)"

    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        ''' Quit command - Exit the program '''
        return True

    def do_EOF(self, arg):
        ''' Quit command - Use CTRL+D to exit the program '''
        print("")
        return True

    def emptyline(self):
        ''' Empty line handling - ENTER shouldn't execute anything '''
        pass

    def do_create(self, args):
        ''' Create command - Create a new instance of BaseModel '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        ''' Show command - Display the string representation of an instance '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        ''' Destroy command - Delete an instance based on class name and ID '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            del obj[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        ''' All command - Display string representation of all instances '''
        storage.reload()
        json_dict = []
        obj_dict = storage.all()
        if args == "":
            for key, value in obj_dict.items():
                json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        arg = shlex.split(args)
        if arg[0] in HBNBCommand.All_class_dict.keys():
            for key, value in obj_dict.items():
                if arg[0] in key:
                    json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        ''' Update command - Modify attributes of an instance '''
        if not args:
            print("** class name missing **")
            return
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])
            print(d_type)
            obj_dict[arg[2]] = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
        storage.save()

    def do_count(self, args):
        ''' Count command - Count instances of a specific class '''
        obj = storage.all()
        cnt = 0
        for key in obj:
            if args in key:
                cnt += 1
        print(cnt)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

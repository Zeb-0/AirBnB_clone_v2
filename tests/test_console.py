#!/usr/bin/python3
"""Module console.py - a command-line interface for Holberton AirBnB"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """General Class for HBNBCommand"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    def do_quit(self, arg):
        """Exit method for quit typing"""
        exit()

    def do_EOF(self, arg):
        """Exit method for EOF"""
        print('')
        exit()

    def emptyline(self):
        """Method to pass when emptyline entered"""
        pass

    def do_create(self, arg):
        """Create a new instance"""
        if len(arg) == 0:
            print('** class name missing **')
            return

        new = None
        if arg in self.classes:
            new = self.classes[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Method to print instance"""
        if len(arg) == 0:
            print('** class name missing **')
            return

        class_name, instance_id = arg.split()[0], None
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg.split()) > 1:
            instance_id = arg.split()[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                instance = storage.all()[key]
                print(instance)
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_destroy(self, arg):
        """Method to delete instance with class and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return

        class_name, instance_id = arg.split()[0], None
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg.split()) > 1:
            instance_id = arg.split()[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
        else:
            print('** instance id missing **')

    def do_all(self, arg):
        """Method to print all instances"""
        instances = []

        if len(arg) == 0:
            instances = [str(a) for a in storage.all().values()]
        elif arg in self.classes:
            instances = [str(a) for b, a in storage.all().items() if arg in b]
        else:
            print("** class doesn't exist **")
            return

        print(instances)

    def do_update(self, arg):
        """Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return

        class_name, instance_id = arg[0], None
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            instance_id = arg[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

    def test_help_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', side_effect=['help show', 'EOF']):
                self.console.cmdloop()
                self.assertFalse("Show command" in mock_stdout.getvalue())

if __name__ == '__main__':
    HBNBCommand().cmdloop()

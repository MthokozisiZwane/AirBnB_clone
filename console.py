#!/usr/bin/python3
"""Command Interpreter Module"""

import cmd
import models
from models import storage
from models.base_model3 import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command intepreter class
    """
    prompt = "(hbnb) "

    def emptyline():
        """
        If the input is empty
        """
        pass

    def do_quit(self, arg):
        """
        command to quit or exit the program

        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program

        """
        print("")
        return True

    def do_create(self, arg):
        """
        creates a new instance of BaseModel
        """
        args = arg.split()
        if len(args) == 0:
            print("** class is missing **")
            return

        try:
            new_instance = models.classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance_key = "{}.{}".format(args[0], args[1])
            print(models.storage.all()[instance_key])
        except KeyError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance_key = "{}.{}".format(args[0], args[1])
            del models.storage.all()[instance_key]
            models.storage.save()
        except KeyError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of an instance
        """
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in models.storage.all().values()])
        else:
            try:
                print([str(value) for key, value in
                       models.storage.all().items()
                       if key.startswith(args[0])])
            except KeyError:
                print("** class doesn't exist **")

    def do_count(self, arg):
        """

        Counts the number of instances of a class

        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        instances_count = storage.count(class_name)
        print(instances_count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance_key = "{}.{}".format(args[0], args[1])
            instance = models.storage.all()[instance_key]
            setattr(instance, args[2], args[3][1:-1])
            models.storage.save()
        except KeyError:
            print("** class doesn't exist **")

        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** no instance found **")

    def do_update_dict(self, arg):
        """
        Updates an instance based on the class name and id
        by updating with a dictionary.

        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            instance_key = "{}.{}".format(args[0], args[1])
            instance = models.storage.all()[instance_key]
            attribute_dict = eval(args[2])
            for k, v in attribute_dict.items():
                setattr(instance, k, v)
            models.storage.save()
        except KeyError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except Exception:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

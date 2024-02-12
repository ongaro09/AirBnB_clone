#!/usr/bin/python3
""" This module contains the command line interpreter for the program """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class implements the command line interpreter """
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit the program """
        return True

    def do_EOF(self, arg):
        """ Exit the command interface """
        print("")
        return True

    def emptyline(self):
        """ Do nothing when an empty line is entered """
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if not arg:
            print("** Missing class name **")
            return
        elif arg not in HBNBCommand.class_dict:
            print("** Class doesn't exist **")
        else:
            new_instance = HBNBCommand.class_dict[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Show instance based on class name and id """
        args = arg.split()

        if not arg:
            print("** Missing class name **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** Class doesn't exist **")
            return
        elif len(args) == 1:
            print("** Missing instance id **")
        else:
            target_class, target_id = args[0], args[1]
            target_key = "{}.{}".format(target_class, target_id)
            all_obj = storage.all()

            if target_key not in all_obj:
                print("** No instance found **")
            else:
                target_instance_dict = all_obj[target_key]
                print(target_instance_dict)

    def do_destroy(self, arg):
        """ Delete an instance based on class name and id """
        args = arg.split()

        if not arg:
            print("** Missing class name **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** Class doesn't exist **")
            return
        elif len(args) == 1:
            print("** Missing instance id **")
        else:
            target_class, target_id = args[0], args[1]
            target_key = "{}.{}".format(target_class, target_id)
            if target_key not in storage.all():
                print("** No instance found **")
            else:
                del storage.all()[target_key]
                storage.save()

    def do_all(self, arg):
        """ Show all instances based on class name """
        args = arg.split()
        instances_to_print = []

        if not arg:
            for instance in storage.all().values():
                instances_to_print.append(str(instance))
        elif args[0] not in HBNBCommand.class_dict:
            print("** Class doesn't exist **")
            return
        else:
            for key, instance in storage.all().items():
                if args[0] in key:
                    instances_to_print.append(str(instance))

        print(instances_to_print)

    def do_update(self, arg):
        """ Update an instance based on class name and id """
        args = arg.split()

        if not arg:
            print("** Missing class name **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** Class doesn't exist **")
            return
        elif len(args) == 1:
            print("** Missing instance id **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** No instance found **")
            return
        elif len(args) == 2:
            print("** Missing attribute name **")
            return
        elif len(args) == 3:
            print("** Missing value **")
            return
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            attribute_value = args[3].strip('\"').strip('\'')
            attribute_type = type(eval(args[3]))
            setattr(storage.all()[instance_key], args[2],
                    attribute_type(attribute_value))
            storage.all()[instance_key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()


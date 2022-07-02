#!/usr/bin/python3
"""Console"""

import cmd
from click import prompt
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ Command Interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Type EOF to exit the command interpreter"""
        return True

    def do_quit(self, arg):
        """Type Exit to exit the command interpreter"""
        return True

    def emptyline(self):
        """Do not execute nothing """
        pass

    def do_create(self, args):
        """Creates a new Instance"""
        if not (args):
            print("** class name missing **")
        elif args not in storage.class_arb():
            print(args)
            #print(classes.keys())
            print("** class doesn't exist **")
        else:
            print("Save")
            print(args)
            ins = storage.class_arb()[args]()
            print(type(ins))
            ins.save()
            print(ins.id)


    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        pass

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        pass

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        pass

    def do_updated(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        pass

    """def accept_class(self):
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        accept_class = { 'BaseModel': BaseModel,
                    'User': User,
                    'Place': Place,
                    'State': State,
                    'City': City, 
                    'Amenity': Amenity, 
                    'Review': Review
                    }

        return accept_class"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()
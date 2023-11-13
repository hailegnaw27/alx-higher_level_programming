#!/usr/bin/python3
""" Base class """

import json
import os

class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list represented by json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy instance
        else:
            dummy = cls(1)  # Create a dummy instance
        dummy.update(**dictionary)  # Use update method to assign real values
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []

        with open(filename, mode="r", encoding="utf-8") as file:
            json_string = file.read()
            dictionaries = cls.from_json_string(json_string)
            instances = [cls.create(**dict_) for dict_ in dictionaries]
            return instances

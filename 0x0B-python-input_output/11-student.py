#!/usr/bin/python3
"""
Module for Student class.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object.

        Args:
        - first_name: string containing the student's first name
        - last_name: string containing the student's last name
        - age: integer containing the student's age

        Returns:
        - Nothing.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the object,
        filtering the attributes to be included.

        Args:
        - attrs (optional): list of attribute names to be included
                            in the dictionary

        Returns:
        - A dictionary containing the attributes of the object.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: self.__dict__[attr] for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the object with those from a dictionary.

        Args:
        - json: dictionary containing attribute names and values

        Returns:
        - Nothing.
        """
        for attr in json:
            setattr(self, attr, json[attr])

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

    def to_json(self):
        """
        Retrieves a dictionary representation of the object.

        Args:
        - None

        Returns:
        - A dictionary containing the attributes of the object.
        """
        return self.__dict__

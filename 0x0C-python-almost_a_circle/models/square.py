#!/usr/bin/python3
""" Square class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns attributes to the instance """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """ Returns the string representation of Square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

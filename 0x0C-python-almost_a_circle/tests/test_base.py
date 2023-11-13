import unittest
import sys
from io import StringIO
import pep8
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    def setUp(self):
        sys.stdout = StringIO()
        Base._Base__nb_objects = 0

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "Found code style errors (and warnings).")

    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(100)
        self.assertEqual(b3.id, 100)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_rectangle_attributes(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)

        r2 = Rectangle(5, 15, 25, 30)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 15)
        self.assertEqual(r2.x, 25)
        self.assertEqual(r2.y, 30)

    def test_rectangle_area(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

        r2 = Rectangle(3, 7)
        self.assertEqual(r2.area(), 21)

    def test_rectangle_display(self):
        r1 = Rectangle(3, 4)
        output = StringIO()
        sys.stdout = output
        r1.display()
        self.assertEqual(output.getvalue(), '###\n###\n###\n###\n')

        r2 = Rectangle(2, 2, 2, 2)
        output = StringIO()
        sys.stdout = output
        r2.display()
        self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n')

    def test_square_attributes(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

        s2 = Square(10, 2, 3)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)

    def test_square_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_base_to_json_string(self):
        r1 = Rectangle(10, 20, 5, 10)
        r1_dict = r1.to_dictionary()
        r1_json = Base.to_json_string([r1_dict])
        self.assertEqual(type(r1_json), str)
        self.assertCountEqual(json.loads(r1_json), '[{"x": 5, "width": 10, "id": 1, "height": 20, "y": 10}]')

        s1 = Square(5, 2, 3)
        s1_dict = s1.to_dictionary()
        s1_json = Base.to_json_string([s1_dict])
        self.assertEqual(type(s1_json), str)
        self.assertCountEqual(json.loads(s1_json), '[{"x": 2, "size": 5, "id": 1, "y": 3}]')

    def test_base_from_json_string(self):
        json_str = '[{"x": 5, "width": 10, "id": 1, "height": 20, "y": 10}]'
        json_list = Base.from_json_string(json_str)
        self.assertIsInstance(json_list, list)
        self.assertEqual(len(json_list), 1)
        self.assertCountEqual(json_list, [{'x': 5, 'width': 10, 'id': 1, 'height': 20, 'y': 10}])

        json_str = '[{"x": 2, "size": 5, "id": 1, "y": 3}]'
        json_list = Base.from_json_string(json_str)
        self.assertIsInstance(json_list, list)
        self.assertEqual(len(json_list), 1)
        self.assertCountEqual(json_list, [{'x': 2, 'size': 5, 'id': 1, 'y': 3}])

    def test_base_save_to_file(self):
        r1 = Rectangle(10, 20, 5, 10)

        Rectangle.save_to_file([r1])

        with open('Rectangle.json', 'r') as file:
            data = file.read()
            self.assertEqual(data, '[{"x": 5, "width": 10, "id": 1, "height": 20, "y": 10}]')

        s1 = Square(5, 2, 3)

        Square.save_to_file([s1])

        with open('Square.json', 'r') as file:
            data = file.read()
            self.assertEqual(data, '[{"x": 2, "size": 5, "id": 1, "y": 3}]')

    def test_base_load_from_file(self):
        r1 = Rectangle(10, 20, 5, 10)
        r2 = Rectangle(5, 5)

        Rectangle.save_to_file([r1, r2])

        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertCountEqual(loaded_rectangles, [{'x': 5, 'width': 10, 'id': 1, 'height': 20, 'y': 10},
                                                  {'x': 0, 'width': 5, 'id': 2, 'height': 5, 'y': 0}])

        s1 = Square(5, 2, 3)
        s2 = Square(3)

        Square.save_to_file([s1, s2])

        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares, list)
        self.assertCountEqual(loaded_squares, [{'x': 2, 'size': 5, 'id': 1, 'y': 3},
                                               {'x': 0, 'size': 3, 'id': 2, 'y': 0}])

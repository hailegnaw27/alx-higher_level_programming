import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test cases for rectangle area
        rect1 = Rectangle(3, 4)
        self.assertEqual(rect1.area(), 12)
        # Add more test cases here

    def test_perimeter(self):
        # Test cases for rectangle perimeter
        rect1 = Rectangle(3, 4)
        self.assertEqual(rect1.perimeter(), 14)
        # Add more test cases here

if __name__ == "__main__":
    unittest.main()

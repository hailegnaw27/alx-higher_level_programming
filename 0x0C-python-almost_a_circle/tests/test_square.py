import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        # Test cases for square area
        square1 = Square(5)
        self.assertEqual(square1.area(), 25)
        # Add more test cases here

    def test_perimeter(self):
        # Test cases for square perimeter
        square1 = Square(5)
        self.assertEqual(square1.perimeter(), 20)
        # Add more test cases here

if __name__ == "__main__":
    unittest.main()

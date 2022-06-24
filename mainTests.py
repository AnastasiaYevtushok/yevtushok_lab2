import unittest
import main


class SquareTest(unittest.TestCase):
    def test_area(self):
        expected = 16
        area = main.Square(4).area()
        self.assertEqual(expected, area)

    def test_perimeter(self):
        expected = 16
        perimeter = main.Square(4).perimeter()
        self.assertEqual(expected, perimeter)


class CircleTest(unittest.TestCase):
    def test_area(self):
        expected = 113.1
        area = round(main.Circle(6).area(), 2)
        self.assertEqual(expected, area)

    def test_perimeter(self):
        expected = 37.7
        perimeter = round(main.Circle(6).perimeter(), 2)
        self.assertEqual(expected, perimeter)


class RhombusTest(unittest.TestCase):
    def test_area(self):
        expected = 25
        area = main.Rhombus(10, 5).area()
        self.assertEqual(expected, area)

    def test_perimeter(self):
        expected = 23.3
        perimeter = round(main.Rhombus(10, 6).perimeter(), 1)
        self.assertEqual(expected, perimeter)


class NameTest(unittest.TestCase):
    def test_name(self):
        expected = "Square,Circle,Rhombus"
        name = main.Square(0).__str__() + "," + main.Circle(0).__str__() + "," + main.Rhombus(0, 0).__str__()
        self.assertEqual(expected, name)


class ValidationTest(unittest.TestCase):
    def test_circle_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Circle(-5)
        self.assertTrue("Name cannot be lower then 0", actual)

    def test_square_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Square(-15)
        self.assertTrue("Name cannot be lower then 0", actual)

    def test_rhombus_validation(self):
        with self.assertRaises(ValueError) as actual:
            main.Rhombus(-5, 7)
        self.assertTrue("Name cannot be lower then 0", actual)

import math


def square_area(side):
    """Returns the area of a square"""
    return side * side


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height) / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1 * diagonal_2)/2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return height*((base_minor+base_major)/2)


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter * apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return 3.1416 * radius ** 2


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.side = 10.0
            self.base = 10.0
            self.height = 25.0
            self.diagonal_1 = 25.0
            self.diagonal_2 = 25.0
            self.base_minor = 25.0
            self.base_major = 40.0
            self.perimeter = 200.0
            self.apothem = 20.0
            self.radius = 100

        def test_square_area(self):
            self.assertEqual(self.side*self.side, square_area(self.side))  # Make this test first...

        def test_rectangle_area(self):
            self.assertEqual(self.base*self.height, rectangle_area(self.base, self.height))

        def test_triangle_area(self):
            self.assertEqual((self.base * self.height)/2, triangle_area(self.base, self.height))

        def test_rhombus_area(self):
            self.assertEqual((self.diagonal_1*self.diagonal_2)/2, rhombus_area(self.diagonal_1, self.diagonal_2))

        def test_trapezoid_area(self):
            self.assertEqual(self.height*((self.base_minor+self.base_major)/2),
                             trapezoid_area(self.base_minor, self.base_major, self.height))

        def test_regular_polygon_area(self):
            self.assertEqual((self.perimeter*self.apothem)/2, regular_polygon_area(self.perimeter, self.apothem))

        def test_circumference_area(self):
            self.assertEqual(3.1416*self.radius**2, circumference_area(self.radius))

        def tearDown(self):
            del(self.side)
            del(self.base)
            del(self.height)
            del(self.diagonal_1)
            del(self.diagonal_2)

    unittest.main()

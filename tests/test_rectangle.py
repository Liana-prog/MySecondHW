from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


class TestRectangle:
    def test_rectangle_perimeter(self):
        rectangle = Rectangle(1, 2)
        assert rectangle.perimeter == 6

    def test_rectangle_area(self):
        rectangle = Rectangle(1, 2)
        assert rectangle.area == 2

    @pytest.mark.parametrize('figure', [Square(1), Circle(1), Triangle(1, 1, 1)])
    def test_rectangle_with_figures(self, figure):
        rectangle = Rectangle(1, 2)
        assert rectangle.add_area(figure) == figure.area + rectangle.area

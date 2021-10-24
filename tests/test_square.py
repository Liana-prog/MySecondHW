from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


class TestSquare:
    def test_square_perimeter(self):
        square = Square(1)
        assert square.perimeter == 4

    def test_square_area(self):
        square = Square(1)
        assert square.area == 1

    @pytest.mark.parametrize('figure', [Rectangle(1, 2), Circle(1), Triangle(1, 1, 1)])
    def test_square_with_figures(self, figure):
        square = Square(1)
        assert square.add_area(figure) == figure.area + square.area

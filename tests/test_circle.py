from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


class TestCircle:
    def test_circle_perimeter(self):
        circle = Circle(10)
        assert circle.perimeter == 62.83185307179586

    def test_circle_area(self):
        circle = Circle(10)
        assert circle.area == 314.1592653589793

    @pytest.mark.parametrize('figure', [Square(1), Triangle(1, 1, 1), Rectangle(1, 2)])
    def test_circle_with_figures(self, figure):
        circle = Circle(10)
        assert circle.add_area(figure) == figure.area + circle.area

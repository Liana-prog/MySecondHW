from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


class TestTriangle:
    def test_triangle_perimeter(self):
        triangle = Triangle(1, 1, 1)
        assert triangle.perimeter == 3

    def test_triangle_area(self):
        triangle = Triangle(1, 1, 1)
        assert triangle.area == 0.4330127018922193+0j

    @pytest.mark.parametrize('figure', [Square(1), Circle(1), Rectangle(1, 2)])
    def test_triangle_with_figures(self, figure):
        triangle = Triangle(1, 1, 1)
        assert triangle.add_area(figure) == figure.area + triangle.area

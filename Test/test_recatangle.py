import pytest
from Fixture import sample_rectangle
from Rectangle import Rectangle
from  ShapeUtils import ShapeActions
from point import Point


def test_rectangle_width(sample_rectangle):
    assert sample_rectangle.get_width() == 7

def test_rectangle_height(sample_rectangle):
    assert sample_rectangle.get_height() == 3

def test_rectangle_area(sample_rectangle):
    assert sample_rectangle.get_area() == 21


def test_rectangle_str(sample_rectangle):
    assert str(sample_rectangle) == "Rectangle(Point(3,5),Point(10,8))"


def test_move_shape(sample_rectangle):
    assert str(sample_rectangle) == "Rectangle(Point(3,5),Point(10,8))"

    ShapeActions.move_shape(sample_rectangle, (-1, -1), (2, 2))
    assert str(sample_rectangle) == "Rectangle(Point(2,4),Point(12,10))"



def test_invalid_rectangle_coordinates():
    with pytest.raises(ValueError, match="Invalid rectangle coordinates. Coordinates must be within \(0, 0\) and \(2240, 1080\)"):
        rectangle = Rectangle(Point(3000, 5), Point(4000, 8))
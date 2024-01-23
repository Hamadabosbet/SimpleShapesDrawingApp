from point import Point
from Fixture import sample_point



def test_point_str(sample_point):
    assert str(sample_point) == "Point(3,5)"

def test_point_from_string(sample_point):
    point_str = str(sample_point)
    point = Point.from_string(point_str)
    assert isinstance(point, Point)
    assert point.x == 3
    assert point.y == 5



import pytest
from point import Point
from Rectangle import Rectangle


@pytest.fixture
def sample_point():
    return Point(3, 5)

@pytest.fixture
def sample_rectangle():
    point1 = Point(3, 5)
    point2 = Point(10, 8)
    return Rectangle(point1, point2)

@pytest.fixture
def sample_rectangle2():
    point1 = Point(3000, 5)
    point2 = Point(4000, 8)
    return Rectangle(point1, point2)

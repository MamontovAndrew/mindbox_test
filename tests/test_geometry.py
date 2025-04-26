import math
import pytest
from geometry import Circle, Triangle, compute_area


def test_circle_area():
    c = Circle(3)
    assert math.isclose(c.area(), math.pi * 9)
    assert math.isclose(compute_area(c), math.pi * 9)


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)
    assert math.isclose(compute_area(t), 6.0)


def test_right_triangle_detection():
    assert Triangle(3, 4, 5).is_right()
    assert not Triangle(3, 4, 6).is_right()


def test_invalid_shapes():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
    with pytest.raises(ValueError):
        Circle(-2)
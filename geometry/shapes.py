from __future__ import annotations
import math
from abc import ABC, abstractmethod
from functools import singledispatch
from typing import Any


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:
        return f"Circle(r={self.radius})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        sides = sorted([a, b, c])
        if any(s <= 0 for s in sides):
            raise ValueError("Стороны должны быть положительными")
        if sides[0] + sides[1] <= sides[2]:
            raise ValueError("Стороны не образуют треугольник")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self, *, rel_tol: float = 1e-9) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=rel_tol)

    def __repr__(self) -> str:
        return f"Triangle({self.a}, {self.b}, {self.c})"


@singledispatch
def compute_area(obj: Any) -> float:
    if isinstance(obj, Shape):
        return obj.area()
    raise TypeError(f"Не знаю, как вычислить площадь объекта типа {type(obj).__name__!s}")


@compute_area.register
def _(circle: Circle) -> float:
    return circle.area()


@compute_area.register
def _(triangle: Triangle) -> float:
    return triangle.area()

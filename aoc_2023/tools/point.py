from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @property
    def unit(self) -> Point:
        x = 0 if self.x == 0 else self.x // abs(self.x)
        y = 0 if self.y == 0 else self.y // abs(self.y)

        return Point(x, y)

    def add(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    @property
    def neighbors(self) -> set[Point]:
        return {
            Point(self.x, self.y - 1),
            Point(self.x + 1, self.y),
            Point(self.x, self.y + 1),
            Point(self.x - 1, self.y),
        }

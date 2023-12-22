from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Brick:
    start: Point
    end: Point
    name: Optional[str]

    def __post_init__(self) -> None:
        assert self.end.x >= self.start.x
        assert self.end.y >= self.start.y
        assert self.end.z >= self.start.z

    @property
    def height(self) -> int:
        return self.end.z + 1 - self.start.z

    def drop(self, z: int) -> Brick:
        return Brick(
            Point(self.start.x, self.start.y, z),
            Point(self.end.x, self.end.y, z + self.height - 1),
            self.name,
        )

    def overlaps(self, other: Brick) -> bool:
        return all(
            [
                self.end.x >= other.start.x,
                self.start.x <= other.end.x,
                self.end.y >= other.start.y,
                self.start.y <= other.end.y,
            ]
        )


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

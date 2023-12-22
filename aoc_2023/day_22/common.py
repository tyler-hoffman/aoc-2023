from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Brick:
    start: Point
    end: Point

    def __post_init__(self) -> None:
        assert self.end.x >= self.start.x
        assert self.end.y >= self.start.y
        assert self.end.z >= self.start.z


@dataclass
class Point:
    x: int
    y: int
    z: int

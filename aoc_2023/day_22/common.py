from __future__ import annotations
from dataclasses import dataclass, field
from functools import cached_property
from typing import Mapping, Optional


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


@dataclass(frozen=True)
class Analyzer:
    bricks: list[Brick] = field(hash=False)

    @cached_property
    def supported_by_map(self) -> Mapping[Brick, set[Brick]]:
        output: dict[Brick, set[Brick]] = {b: set() for b in self.stacked}
        for brick, supports in self.support_map.items():
            for b in supports:
                output[b].add(brick)
        return output

    @cached_property
    def support_map(self) -> Mapping[Brick, set[Brick]]:
        output: dict[Brick, set[Brick]] = {b: set() for b in self.stacked}
        for brick in self.stacked:
            z_above = brick.end.z + 1
            for other in self.bricks_at_level.get(z_above, set()):
                if brick.overlaps(other):
                    output[brick].add(other)
        return output

    @cached_property
    def bricks_at_level(self) -> Mapping[int, set[Brick]]:
        zs = sorted({b.start.z for b in self.stacked})
        by_z: dict[int, set[Brick]] = {z: set() for z in zs}
        for brick in self.stacked:
            by_z[brick.start.z].add(brick)
        return by_z

    @cached_property
    def stacked(self) -> list[Brick]:
        output = list[Brick]()

        for brick in self.sorted_vertically:
            found_it = False
            for i in range(len(output) - 1, -1, -1):
                other = output[i]
                if brick.overlaps(other):
                    found_it = True
                    output.append(brick.drop(other.end.z + 1))
                    break
            if not found_it:
                output.append(brick.drop(1))
            output.sort(key=lambda b: (b.end.z, b.start.y, b.start.x))

        return output

    @cached_property
    def sorted_vertically(self) -> list[Brick]:
        return sorted(
            self.bricks,
            key=lambda b: (b.start.z, b.start.y, b.start.x),
        )

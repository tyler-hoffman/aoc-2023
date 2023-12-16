from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property
from typing import Optional

from aoc_2023.tools.point import Point

UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)


@dataclass
class Grid:
    chars: list[str]

    def contains(self, point: Point) -> bool:
        return all(
            [
                point.x >= 0,
                point.x < self.width,
                point.y >= 0,
                point.y < self.height,
            ]
        )

    @cached_property
    def width(self) -> int:
        return len(self.chars[0])

    @cached_property
    def height(self) -> int:
        return len(self.chars)

    def get_energized(self, start: Beam) -> int:
        energized = set[Point]()
        seen = {start}
        to_check = [start]
        while to_check:
            beam = to_check.pop()
            energized.add(beam.pos)

            tile = self.chars[beam.pos.y][beam.pos.x]
            next_beams = list[Beam]()
            match tile:
                case ".":
                    next_beams.append(beam.move())
                case "|":
                    if beam.direction in {LEFT, RIGHT}:
                        next_beams.append(beam.move(UP))
                        next_beams.append(beam.move(DOWN))
                    else:
                        next_beams.append(beam.move())
                case "-":
                    if beam.direction in {UP, DOWN}:
                        next_beams.append(beam.move(LEFT))
                        next_beams.append(beam.move(RIGHT))
                    else:
                        next_beams.append(beam.move())
                case "/":
                    if beam.direction == RIGHT:
                        next_beams.append(beam.move(UP))
                    elif beam.direction == LEFT:
                        next_beams.append(beam.move(DOWN))
                    elif beam.direction == UP:
                        next_beams.append(beam.move(RIGHT))
                    else:
                        next_beams.append(beam.move(LEFT))
                case "\\":
                    if beam.direction == RIGHT:
                        next_beams.append(beam.move(DOWN))
                    elif beam.direction == LEFT:
                        next_beams.append(beam.move(UP))
                    elif beam.direction == UP:
                        next_beams.append(beam.move(LEFT))
                    else:
                        next_beams.append(beam.move(RIGHT))
                case _:
                    assert False
            next_beams = [
                b for b in next_beams if b not in seen and self.contains(b.pos)
            ]
            for b in next_beams:
                to_check.append(b)
                seen.add(b)

        return len(energized)


@dataclass(frozen=True)
class Beam:
    pos: Point
    direction: Point

    def move(self, direction: Optional[Point] = None) -> Beam:
        if direction is None:
            direction = self.direction
        return Beam(self.pos.add(direction), direction)

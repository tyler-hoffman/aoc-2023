from dataclasses import dataclass
from functools import cached_property
from typing import Mapping

from aoc_2023.tools.point import Point

UP = Point(0, -1)
RIGHT = Point(1, 0)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


@dataclass
class LoopFinder:
    map: list[list[str]]

    def get_loop(self, start: Point) -> list[Point]:
        output = [start]
        direction = self.get_directions_out(start)[0]
        pos = start.add(direction)
        while pos != start:
            output.append(pos)
            next_char = self.map[pos.y][pos.x]
            direction = self.new_move[(direction, next_char)]
            pos = pos.add(direction)
        return output

    def get_directions_out(self, point: Point) -> list[Point]:
        output = list[Point]()
        for direction in DIRECTIONS:
            p = point.add(direction)
            if self.in_bounds(p):
                key = (direction, self.map[p.y][p.x])
                if key in self.new_move:
                    output.append(direction)

        return output

    def in_bounds(self, point: Point) -> bool:
        return all(
            [
                point.x >= 0,
                point.y >= 0,
                point.x < len(self.map[0]),
                point.y < len(self.map),
            ]
        )

    @cached_property
    def new_move(self) -> Mapping[tuple[Point, str], Point]:
        return {
            (UP, "|"): UP,
            (UP, "F"): RIGHT,
            (UP, "7"): LEFT,
            (RIGHT, "J"): UP,
            (RIGHT, "-"): RIGHT,
            (RIGHT, "7"): DOWN,
            (DOWN, "J"): LEFT,
            (DOWN, "|"): DOWN,
            (DOWN, "L"): RIGHT,
            (LEFT, "F"): DOWN,
            (LEFT, "-"): LEFT,
            (LEFT, "L"): UP,
        }

    @cached_property
    def start(self) -> Point:
        for y, line in enumerate(self.map):
            for x, ch in enumerate(line):
                if ch == "S":
                    return Point(x, y)
        assert False

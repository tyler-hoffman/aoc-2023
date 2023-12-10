from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_10.parser import Parser
from aoc_2023.tools.point import Point


UP = Point(0, -1)
RIGHT = Point(1, 0)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


@dataclass
class Day10PartASolver:
    map: list[list[str]]

    @property
    def solution(self) -> int:
        loop = self.get_loop(self.start)
        return self.distance_to_furtheset(loop, self.start)

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

    def distance_to_furtheset(self, loop: list[Point], start: Point) -> int:
        return len(loop) // 2

    @cached_property
    def start(self) -> Point:
        for y, line in enumerate(self.map):
            for x, ch in enumerate(line):
                if ch == "S":
                    return Point(x, y)
        assert False


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day10PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

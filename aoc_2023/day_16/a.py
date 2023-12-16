from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_16.common import RIGHT, Beam, Grid
from aoc_2023.day_16.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day16PartASolver:
    chars: list[str]

    @property
    def solution(self) -> int:
        return self.grid.get_energized(Beam(Point(0, 0), RIGHT))

    @cached_property
    def grid(self) -> Grid:
        return Grid(self.chars)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

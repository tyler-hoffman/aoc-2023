from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_16.common import DOWN, LEFT, RIGHT, UP, Beam, Grid
from aoc_2023.day_16.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day16PartBSolver:
    chars: list[str]

    @cached_property
    def grid(self) -> Grid:
        return Grid(self.chars)

    @property
    def solution(self) -> int:
        counts = set[int]()
        g = self.grid
        for y in range(g.height):
            counts.add(g.get_energized(Beam(Point(0, y), RIGHT)))
            counts.add(g.get_energized(Beam(Point(g.width - 1, y), LEFT)))
        for x in range(g.width):
            counts.add(g.get_energized(Beam(Point(x, 0), DOWN)))
            counts.add(g.get_energized(Beam(Point(x, g.height - 1), UP)))
        return max(counts)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day16PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_16/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

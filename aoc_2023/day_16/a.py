from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_16.common import Grid
from aoc_2023.day_16.parser import Parser


@dataclass
class Day16PartASolver:
    chars: list[str]

    @property
    def solution(self) -> int:
        return -1

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

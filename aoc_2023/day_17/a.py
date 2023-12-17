from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_17.parser import Parser


@dataclass
class Day17PartASolver:
    grid: list[list[int]]

    @property
    def solution(self) -> int:
        return -1

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

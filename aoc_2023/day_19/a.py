from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_19.common import Data, Part, Workflow
from aoc_2023.day_19.parser import Parser


@dataclass
class Day19PartASolver:
    data: Data

    @property
    def solution(self) -> int:
        return -1

    @cached_property
    def workflows(self) -> list[Workflow]:
        return self.data.workflows

    @cached_property
    def parts(self) -> list[Part]:
        return self.data.parts


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day19PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

import re
from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_03.common import Analyzer
from aoc_2023.day_03.parser import Parser


@dataclass
class Day03PartASolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        return sum(v.value for v in self.analyzer.part_numbers)

    @cached_property
    def analyzer(self) -> Analyzer:
        return Analyzer(self.lines)

    @cached_property
    def number_regex(self) -> re.Pattern:
        return re.compile(r"(\d+)")

    @cached_property
    def symbol_regex(self) -> re.Pattern:
        return re.compile(r"[^0-9.]")


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

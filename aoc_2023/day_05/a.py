from dataclasses import dataclass
from aoc_2023.day_05.common import Data
from aoc_2023.day_05.parser import Parser


@dataclass
class Day05PartASolver:
    data: Data

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day05PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

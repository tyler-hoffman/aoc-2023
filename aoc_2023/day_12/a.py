from dataclasses import dataclass
from aoc_2023.day_12.common import Record
from aoc_2023.day_12.parser import Parser


@dataclass
class Day12PartASolver:
    data: list[Record]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

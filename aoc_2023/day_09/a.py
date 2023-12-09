from dataclasses import dataclass
from aoc_2023.day_09.parser import Parser


@dataclass
class Day09PartASolver:
    data: list[list[int]]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

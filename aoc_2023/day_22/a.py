from dataclasses import dataclass
from aoc_2023.day_22.common import Brick
from aoc_2023.day_22.parser import Parser


@dataclass
class Day22PartASolver:
    bricks: list[Brick]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day22PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

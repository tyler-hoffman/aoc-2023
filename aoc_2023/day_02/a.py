from dataclasses import dataclass
from aoc_2023.day_02.common import Game
from aoc_2023.day_02.parser import Parser


@dataclass
class Day02PartASolver:
    games: list[Game]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartASolver(
        data,
    )

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

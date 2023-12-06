from dataclasses import dataclass
from math import prod
from aoc_2023.day_06.common import Race, solutions_for_race
from aoc_2023.day_06.parser import Parser


@dataclass
class Day06PartASolver:
    races: list[Race]

    @property
    def solution(self) -> int:
        solutions_per_race = [solutions_for_race(r) for r in self.races]
        return prod(s for s in solutions_per_race)


def solve(input: str) -> int:
    races = Parser.parse(input)
    solver = Day06PartASolver(races)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_06.common import Race, solutions_for_race
from aoc_2023.day_06.parser import Parser


@dataclass
class Day06PartBSolver:
    races: list[Race]

    @property
    def solution(self) -> int:
        return solutions_for_race(self.big_race)

    @cached_property
    def big_race(self) -> Race:
        time = self.cram_numbers_together([r.time for r in self.races])
        distance = self.cram_numbers_together([r.distance for r in self.races])
        return Race(time=time, distance=distance)

    def cram_numbers_together(self, numbers: list[int]) -> int:
        return int("".join(str(x) for x in numbers))


def solve(input: str) -> int:
    races = Parser.parse(input)
    solver = Day06PartBSolver(races)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_06/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

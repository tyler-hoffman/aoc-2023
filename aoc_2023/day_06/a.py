from dataclasses import dataclass
from math import prod
from aoc_2023.day_06.common import Race
from aoc_2023.day_06.parser import Parser


@dataclass
class Day06PartASolver:
    races: list[Race]

    @property
    def solution(self) -> int:
        solutions_per_race = [self.solutions_for_race(r) for r in self.races]
        return prod(len(s) for s in solutions_per_race)

    def solutions_for_race(self, race: Race) -> set[int]:
        hold_times = set[int]()
        for t in range(race.time + 1):
            speed = t
            boat_time = race.time - t
            dist = boat_time * speed
            if dist > race.distance:
                hold_times.add(t)

        return hold_times


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

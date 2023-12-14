from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_13.common import MapSolver
from aoc_2023.day_13.parser import Parser


@dataclass
class Day13PartBSolver:
    land_maps: list[list[list[str]]]

    @property
    def solution(self) -> int:
        return sum(solver.score for solver in self.map_solvers)

    @cached_property
    def map_solvers(self) -> list[MapSolver]:
        return [MapSolver(i, land_map, 1) for i, land_map in enumerate(self.land_maps)]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day13PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_13/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

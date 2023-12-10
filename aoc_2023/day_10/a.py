from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_10.common import LoopFinder
from aoc_2023.day_10.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day10PartASolver:
    map: list[list[str]]

    @property
    def solution(self) -> int:
        loop = self.loop_finder.get_loop(self.loop_finder.start)
        return self.distance_to_furtheset(loop, self.loop_finder.start)

    @cached_property
    def loop_finder(self) -> LoopFinder:
        return LoopFinder(self.map)

    def distance_to_furtheset(self, loop: list[Point], start: Point) -> int:
        return len(loop) // 2


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day10PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

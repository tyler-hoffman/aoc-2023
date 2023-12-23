from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_22.common import Analyzer, Brick
from aoc_2023.day_22.parser import Parser


@dataclass
class Day22PartASolver:
    bricks: list[Brick]

    @property
    def solution(self) -> int:
        support_map = self.analyzer.support_map
        support_count: dict[Brick, int] = {b: 0 for b in self.analyzer.stacked}
        for supported in support_map.values():
            for brick in supported:
                support_count[brick] += 1

        to_disintigrate = set[Brick]()
        for brick, supports in support_map.items():
            if not any([b for b in supports if support_count[b] == 1]):
                to_disintigrate.add(brick)

        return len(to_disintigrate)

    @cached_property
    def analyzer(self) -> Analyzer:
        return Analyzer(self.bricks)


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

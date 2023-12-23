from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2023.day_22.common import Analyzer, Brick
from aoc_2023.day_22.parser import Parser


@dataclass(frozen=True)
class Day22PartBSolver:
    bricks: list[Brick] = field(hash=False)

    @property
    def solution(self) -> int:
        fall_counts = [self.fall_count(b) for b in self.analyzer.stacked]
        return sum(fall_counts)

    @cache
    def fall_count(self, to_remove: Brick) -> int:
        nuked = {to_remove}
        for z, bricks in self.analyzer.bricks_at_level.items():
            if z <= to_remove.start.z:
                continue
            for brick in bricks:
                if all(b in nuked for b in self.analyzer.supported_by_map[brick]):
                    nuked.add(brick)
        return len(nuked) - 1

    @cached_property
    def analyzer(self) -> Analyzer:
        return Analyzer(self.bricks)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day22PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

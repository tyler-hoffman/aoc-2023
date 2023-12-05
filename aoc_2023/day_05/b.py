from dataclasses import dataclass
from functools import cached_property
from itertools import batched
from aoc_2023.day_05.common import Data, Range
from aoc_2023.day_05.parser import Parser


@dataclass
class Day05PartBSolver:
    data: Data

    @property
    def solution(self) -> int:
        location_ranges = set[Range]()
        for range in self.seed_ranges:
            location_ranges.update(self.get_location_ranges(range))

        for range in location_ranges:
            assert range.end > range.start
        return min(range.start for range in location_ranges)

    @cached_property
    def seed_ranges(self) -> set[Range]:
        ranges = set[Range]()
        for start, count in batched(self.data.seeds, 2):
            ranges.add(Range(start, start + count))
        return ranges

    def get_location_ranges(self, range: Range) -> set[Range]:
        ranges = set[Range]([range])
        for mapping_set in self.data.mapping_sets:
            new_ranges = set[Range]()
            for range in ranges:
                for new_range in (mapping_set.map_range(r) for r in ranges):
                    new_ranges.update(new_range)
            ranges = new_ranges
        return ranges


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day05PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_05/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

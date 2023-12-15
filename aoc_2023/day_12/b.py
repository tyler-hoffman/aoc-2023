from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_12.common import Record, solve_it
from aoc_2023.day_12.parser import Parser


@dataclass(frozen=True)
class Day12PartBSolver:
    original_records: list[Record]

    @cached_property
    def solution(self) -> int:
        return sum(solve_it(r.chars, tuple(r.congruencies)) for r in self.records)

    @cached_property
    def records(self) -> list[Record]:
        return [
            Record(
                chars="?".join([original.chars] * 5),
                congruencies=original.congruencies * 5,
            )
            for original in self.original_records
        ]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

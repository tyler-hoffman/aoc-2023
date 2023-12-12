from dataclasses import dataclass, field
from functools import cached_property
from aoc_2023.day_12.common import Day12Solver, Record
from aoc_2023.day_12.parser import Parser


@dataclass(frozen=True)
class Day12PartASolver(Day12Solver):
    data: list[Record] = field(hash=False)

    @cached_property
    def records(self) -> list[Record]:
        return self.data


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_12.common import Record, solve_it
from aoc_2023.day_12.parser import Parser


@dataclass(frozen=True)
class Day12PartBSolver:
    original_records: list[Record]

    @cached_property
    def solution(self) -> int:
        return sum(
            solve_it(tuple(r.chars), tuple(r.congruencies)) for r in self.records
        )

    @cached_property
    def records(self) -> list[Record]:
        output = list[Record]()
        for record in self.original_records:
            chars = list[str]()
            congruencies = list[int]()
            for _ in range(5):
                chars.extend(record.chars)
                chars.append("?")
                congruencies.extend(record.congruencies)
            chars.pop()
            output.append(Record(chars, congruencies))
        return output


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

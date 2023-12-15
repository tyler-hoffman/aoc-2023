from dataclasses import dataclass
from aoc_2023.day_15.common import hash_it
from aoc_2023.day_15.parser import Parser


@dataclass
class Day15PartASolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        return sum(hash_it(line) for line in self.lines)


def solve(input: str) -> int:
    data = Parser.parse_lines(input)
    solver = Day15PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

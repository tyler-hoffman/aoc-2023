from dataclasses import dataclass
from aoc_2023.day_09.parser import Parser


@dataclass
class Day09PartBSolver:
    lines: list[list[int]]

    @property
    def solution(self) -> int:
        vals = [self.first(line) for line in self.lines]
        return sum(vals)

    @staticmethod
    def first(vals: list[int]) -> int:
        if all([val == 0 for val in vals]):
            return 0
        diff = Day09PartBSolver.get_diff(vals)
        first_diff = Day09PartBSolver.first(diff)
        return vals[0] - first_diff

    @staticmethod
    def get_diff(vals: list[int]) -> list[int]:
        return [vals[i] - vals[i - 1] for i in range(1, len(vals))]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

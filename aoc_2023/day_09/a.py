from dataclasses import dataclass
from aoc_2023.day_09.parser import Parser


@dataclass
class Day09PartASolver:
    lines: list[list[int]]

    @property
    def solution(self) -> int:
        vals = [self.get_new_last_num(line) for line in self.lines]
        return sum(vals)

    @staticmethod
    def get_new_last_num(vals: list[int]) -> int:
        if all([val == 0 for val in vals]):
            return 0
        diff = Day09PartASolver.get_diff(vals)
        last_diff = Day09PartASolver.get_new_last_num(diff)
        return last_diff + vals[-1]

    @staticmethod
    def get_diff(vals: list[int]) -> list[int]:
        return [vals[i] - vals[i - 1] for i in range(1, len(vals))]


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day09PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_09/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

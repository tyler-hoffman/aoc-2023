from dataclasses import dataclass
from aoc_2023.day_11.common import Day11Solver
from aoc_2023.day_11.parser import Parser


@dataclass
class Day11PartBSolver:
    input: str


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11Solver(data, 1000000)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

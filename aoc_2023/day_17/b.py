from __future__ import annotations
from aoc_2023.day_17.common import Day17Solver
from aoc_2023.day_17.parser import Parser


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day17Solver(data, min_move=4, max_move=10)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_17/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from aoc_2023.day_18.common import Instruction
from aoc_2023.day_18.parser import Parser


@dataclass
class Day18PartASolver:
    instructions: list[Instruction]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day18PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

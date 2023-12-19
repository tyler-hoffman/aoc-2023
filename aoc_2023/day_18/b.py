from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_18.common import (
    Instruction,
    Solver,
)
from aoc_2023.day_18.parser import Parser


@dataclass
class Day18PartBSolver:
    wrong_instructions: list[Instruction]

    @property
    def solution(self) -> int:
        return Solver(self.instructions).solution

    @cached_property
    def solver(self) -> Solver:
        return Solver(self.instructions)

    @cached_property
    def instructions(self) -> list[Instruction]:
        return [self.correct_instruction(inst) for inst in self.wrong_instructions]

    def correct_instruction(self, instruction: Instruction) -> Instruction:
        dist = instruction.color[:5]
        direction = instruction.color[-1]

        DIRECTION_MAP = {
            "0": "R",
            "1": "D",
            "2": "L",
            "3": "U",
        }

        return Instruction(DIRECTION_MAP[direction], int(dist, 16), instruction.color)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day18PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

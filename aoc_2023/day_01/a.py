from dataclasses import dataclass
from typing import Optional
from aoc_2023.day_01.parser import Parser


@dataclass
class Day01PartASolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        return sum(self.line_values)

    @property
    def line_values(self) -> list[int]:
        firsts_and_lasts = [self.first_and_last(line) for line in self.lines]
        return [int(f"{a}{b}") for a, b in firsts_and_lasts]

    def first_and_last(self, line: str) -> tuple[int, int]:
        first: Optional[int] = None
        last: Optional[int] = None

        for ch in line:
            if ch.isdigit():
                first = int(ch)
                break
        for ch in line[::-1]:
            if ch.isdigit():
                last = int(ch)
                break

        assert first is not None and last is not None
        return first, last


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

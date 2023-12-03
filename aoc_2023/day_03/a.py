import re
from dataclasses import dataclass
from functools import cached_property
from aoc_2023.common import Value
from aoc_2023.day_03.parser import Parser


@dataclass
class Day03PartASolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        return sum(v.value for v in self.part_numbers)

    @cached_property
    def height(self) -> int:
        return len(self.lines)

    @cached_property
    def width(self) -> int:
        return len(self.lines[0])

    @cached_property
    def part_numbers(self) -> set[Value]:
        output = set[Value]()
        for value in self.numbers:
            bounds = self.bounding_box(value)
            chars = "".join(bounds)
            if self.symbol_regex.search(chars) is not None:
                output.add(value)
        return output

    def bounding_box(self, value: Value) -> list[str]:
        x1 = max(0, value.start - 1)
        x2 = min(self.width, value.end + 1)
        y1 = max(0, value.line_number - 1)
        y2 = min(self.height, value.line_number + 2)

        return [self.lines[y][x1:x2] for y in range(y1, y2)]

    @cached_property
    def numbers(self) -> set[Value]:
        output = set[Value]()

        for i, line in enumerate(self.lines):
            for m in self.number_regex.finditer(line):
                output.add(
                    Value(
                        value=int(m.group(0)),
                        start=m.start(),
                        end=m.end(),
                        line_number=i,
                    )
                )

        return output

    @cached_property
    def number_regex(self) -> re.Pattern:
        return re.compile(r"(\d+)")

    @cached_property
    def symbol_regex(self) -> re.Pattern:
        return re.compile(r"[^0-9.]")


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

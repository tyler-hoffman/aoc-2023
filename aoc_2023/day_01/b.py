from dataclasses import dataclass
from aoc_2023.day_01.parser import Parser

number_strings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

string_map = {num_string: i + 1 for i, num_string in enumerate(number_strings)} | {
    str(x): x for x in range(10)
}


@dataclass
class Day01PartBSolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        return sum(self.line_values)

    @property
    def line_values(self) -> list[int]:
        firsts_and_lasts = [self.first_and_last(line) for line in self.lines]
        return [int(f"{a}{b}") for a, b in firsts_and_lasts]

    def first_and_last(self, line: str) -> tuple[int, int]:
        indexes = list(range(len(line)))
        first = self.first_instance(line, indexes)
        last = self.first_instance(line, indexes[::-1])

        return first, last

    def first_instance(self, line: str, indexes: list[int]) -> int:
        for i in indexes:
            for string, value in string_map.items():
                if line[i:].startswith(string):
                    return value
        assert False, "we shouldn't get here"


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

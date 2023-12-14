from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_14.parser import Parser


@dataclass
class Day14PartASolver:
    panel: list[list[str]]

    @property
    def solution(self) -> int:
        return sum(self.solve_col(x) for x in range(self.width))

    def solve_col(self, x: int) -> int:
        dest = 0
        output = 0
        for y in range(self.height):
            match self.panel[y][x]:
                case ".":
                    ...
                case "#":
                    dest = y + 1
                case "O":
                    output += self.height - dest
                    dest += 1
                case _:
                    assert False
        return output

    @cached_property
    def width(self) -> int:
        return len(self.panel[0])

    @cached_property
    def height(self) -> int:
        return len(self.panel)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day14PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

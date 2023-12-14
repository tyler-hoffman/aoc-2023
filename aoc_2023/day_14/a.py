from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_14.parser import Parser


@dataclass
class Day14PartASolver:
    panel: list[list[str]]

    @property
    def solution(self) -> int:
        panel = self.tilt_north(self.panel)
        return self.count_north_load(panel)

    def count_north_load(self, panel: list[list[str]]) -> int:
        output = 0
        for x in range(self.width):
            for y in range(self.height):
                if panel[y][x] == "O":
                    output += self.height - y
        return output

    def tilt_north(self, panel: list[list[str]]) -> list[list[str]]:
        output = [["." for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.width):
            dest = 0
            for y in range(self.height):
                match panel[y][x]:
                    case ".":
                        ...
                    case "#":
                        output[y][x] = "#"
                        dest = y + 1
                    case "O":
                        output[dest][x] = "O"
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

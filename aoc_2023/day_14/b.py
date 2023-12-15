from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_14.parser import Parser


@dataclass
class Day14PartBSolver:
    panel: list[list[str]]
    cycles: int = 1000000000

    @property
    def solution(self) -> int:
        seen_at = dict[tuple[tuple[str, ...], ...], int]()

        panel = self.panel
        for i in range(self.cycles):
            panel = self.do_cycle(panel)
            as_tuple = tuple([tuple([x for x in line]) for line in panel])
            if as_tuple in seen_at:
                first_sighted = seen_at[as_tuple]
                cycle_length = i - first_sighted
                cycles_left = self.cycles - i - 1
                offset = cycles_left % cycle_length
                index = first_sighted + offset
                for p, j in seen_at.items():
                    if j == index:
                        return self.count_north_load([[x for x in line] for line in p])
            else:
                seen_at[as_tuple] = i
        return self.count_north_load(panel)

    def do_cycle(self, panel: list[list[str]]) -> list[list[str]]:
        panel = self.tilt_north(panel)
        panel = self.tilt_west(panel)
        panel = self.tilt_south(panel)
        panel = self.tilt_east(panel)
        return panel

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

    def tilt_south(self, panel: list[list[str]]) -> list[list[str]]:
        output = [["." for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.width):
            dest = self.height - 1
            for y in range(self.height - 1, -1, -1):
                match panel[y][x]:
                    case ".":
                        ...
                    case "#":
                        output[y][x] = "#"
                        dest = y - 1
                    case "O":
                        output[dest][x] = "O"
                        dest -= 1
                    case _:
                        assert False
        return output

    def tilt_west(self, panel: list[list[str]]) -> list[list[str]]:
        output = [["." for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            dest = 0
            for x in range(self.width):
                match panel[y][x]:
                    case ".":
                        ...
                    case "#":
                        output[y][x] = "#"
                        dest = x + 1
                    case "O":
                        output[y][dest] = "O"
                        dest += 1
                    case _:
                        assert False
        return output

    def tilt_east(self, panel: list[list[str]]) -> list[list[str]]:
        output = [["." for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            dest = self.width - 1
            for x in range(self.width - 1, -1, -1):
                match panel[y][x]:
                    case ".":
                        ...
                    case "#":
                        output[y][x] = "#"
                        dest = x - 1
                    case "O":
                        output[y][dest] = "O"
                        dest -= 1
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
    solver = Day14PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_14/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

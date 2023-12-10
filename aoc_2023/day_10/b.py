from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_10.common import LoopFinder
from aoc_2023.day_10.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day10PartBSolver:
    map: list[list[str]]

    @property
    def solution(self) -> int:
        expanded = self.expand_map(self.map)
        self.flood_fill_outside(expanded)

        contracted = self.contract_map(expanded)
        total_count = self.width * self.height
        loop_count = len(self.points_in_loop)
        outside_count = sum([sum([1 for x in line if x == "O"]) for line in contracted])

        return total_count - outside_count - loop_count

    def flood_fill_outside(self, the_map: list[list[str]]) -> None:
        """Yeah, I'm mutating the map, sue me"""
        loop_finder = LoopFinder(the_map)
        loop_points = set(loop_finder.get_loop(loop_finder.start))
        definitely_outside = Point(0, 0)
        to_check = [definitely_outside]
        seen = {definitely_outside}
        while to_check:
            checking = to_check.pop()
            the_map[checking.y][checking.x] = "O"
            for n in checking.neighbors:
                if all(
                    [
                        loop_finder.in_bounds(n),
                        n not in seen,
                        n not in loop_points,
                    ]
                ):
                    seen.add(n)
                    to_check.append(n)

    @cached_property
    def loop_finder(self) -> LoopFinder:
        return LoopFinder(self.map)

    @cached_property
    def first_outside_horizontal(self) -> Point:
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                p = Point(x, y)
                if p in self.points_in_loop:
                    return p
        assert False

    @cached_property
    def points_in_loop(self) -> set[Point]:
        loop = self.loop_finder.get_loop(self.loop_finder.start)
        return set(loop)

    def expand_map(self, the_map: list[list[str]]) -> list[list[str]]:
        output = [["."] * (self.width * 2 + 1) for _ in range(self.height * 2 + 1)]
        for y in range(len(the_map)):
            for x in range(len(the_map[y])):
                curr = the_map[y][x]
                output[y * 2 + 1][x * 2 + 1] = curr
                if curr in {"L", "|", "J"}:
                    output[y * 2][x * 2 + 1] = "|"
                if curr in {"J", "-", "7"}:
                    output[y * 2 + 1][x * 2] = "-"

        start = self.loop_finder.start
        to_check = [start.add(p) for p in self.loop_finder.get_directions_out(start)]
        for p in to_check:
            if p.y < start.y and the_map[p.y][p.x] in {"7", "F", "|"}:
                output[start.y * 2][start.x * 2 + 1] = "|"
            if p.x < start.x and the_map[p.y][p.x] in {"-", "L", "F"}:
                output[start.y * 2 + 1][start.x * 2] = "-"

        return output

    def contract_map(self, the_map: list[list[str]]) -> list[list[str]]:
        new_width = len(the_map[0]) // 2
        new_height = len(the_map) // 2
        return [
            [the_map[2 * y + 1][2 * x + 1] for x in range(new_width)]
            for y in range(new_height)
        ]

    @cached_property
    def height(self) -> int:
        return len(self.map)

    @cached_property
    def width(self) -> int:
        return len(self.map[0])


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day10PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_10/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_11.parser import Parser
from aoc_2023.tools.point import Point


@dataclass(frozen=True)
class Galaxy:
    id: int
    pos: Point


@dataclass
class Day11PartASolver:
    data: list[list[str]]

    @property
    def solution(self) -> int:
        output = 0
        checked = 0
        for i in range(self.galaxy_count):
            for j in range(i + 1, self.galaxy_count):
                checked += 1
                output += self.shortest_path_by_id(i, j)
        return output

    def shortest_path_by_id(self, i: int, j: int) -> int:
        a = self.expanded_galaxies[i].pos
        b = self.expanded_galaxies[j].pos
        return a.dist(b)

    @cached_property
    def galaxy_count(self) -> int:
        return len(self.original_galaxies)

    @cached_property
    def original_galaxies(self) -> Mapping[int, Galaxy]:
        output = dict[int, Galaxy]()
        current_id = 0
        for y, line in enumerate(self.data):
            for x, ch in enumerate(line):
                if ch == "#":
                    galaxy = Galaxy(current_id, Point(x, y))
                    output[galaxy.id] = galaxy
                    current_id += 1
        return output

    @cached_property
    def expanded_galaxies(self) -> Mapping[int, Galaxy]:
        return {
            id: Galaxy(
                id,
                Point(
                    g.pos.x + self.x_expansions_before[g.pos.x],
                    g.pos.y + self.y_expansions_before[g.pos.y],
                ),
            )
            for id, g in self.original_galaxies.items()
        }

    @cached_property
    def x_expansions_before(self) -> list[int]:
        output = list[int]()
        occupied = set[int]()
        for g in self.original_galaxies.values():
            occupied.add(g.pos.x)
        current_expansions = 0
        for i in range(self.original_width):
            output.append(current_expansions)
            if i not in occupied:
                current_expansions += 1
        return output

    @cached_property
    def y_expansions_before(self) -> list[int]:
        output = list[int]()
        occupied = set[int]()
        for g in self.original_galaxies.values():
            occupied.add(g.pos.y)
        current_expansions = 0
        for i in range(self.original_height):
            output.append(current_expansions)
            if i not in occupied:
                current_expansions += 1
        return output

    @cached_property
    def original_width(self) -> int:
        return len(self.data[0])

    @cached_property
    def original_height(self) -> int:
        return len(self.data)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day11PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_11/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

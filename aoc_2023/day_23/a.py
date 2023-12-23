import sys
from dataclasses import dataclass
from functools import cached_property
from typing import Iterator, Mapping
from aoc_2023.day_23.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day23PartASolver:
    map: Mapping[Point, str]

    @property
    def solution(self) -> int:
        sys.setrecursionlimit(100000)
        return max(self.get_lengths(self.start, set()))

    def get_lengths(self, point: Point, seen: set[Point]) -> Iterator[int]:
        if point == self.goal:
            yield len(seen)
            return

        seen.add(point)
        next_points = {
            p
            for p in self.next_points(point)
            if self.map.get(p, "#") != "#" and p not in seen
        }
        for p in next_points:
            yield from self.get_lengths(p, seen)
        seen.remove(point)

    def next_points(self, point: Point) -> set[Point]:
        match self.map[point]:
            case ".":
                return {n for n in point.neighbors}
            case ">":
                return {point.add(Point(1, 0))}
            case "<":
                return {point.add(Point(-1, 0))}
            case "^":
                return {point.add(Point(0, -1))}
            case "v":
                return {point.add(Point(0, 1))}
            case _:
                assert False

    @cached_property
    def start(self) -> Point:
        points = [p for p, k in self.map.items() if p.y == 0 and k == "."]
        assert len(points) == 1
        return points[0]

    @cached_property
    def goal(self) -> Point:
        points = [p for p, k in self.map.items() if p.y == self.y_max and k == "."]
        assert len(points) == 1
        return points[0]

    @cached_property
    def x_max(self) -> int:
        return max(p.x for p in self.map.keys())

    @cached_property
    def y_max(self) -> int:
        return max(p.y for p in self.map.keys())


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day23PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

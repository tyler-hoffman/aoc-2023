from dataclasses import dataclass
from functools import cached_property
from typing import Iterator, Mapping
from aoc_2023.day_23.parser import Parser
from aoc_2023.tools.point import Point


@dataclass(frozen=True)
class Segment:
    a: Point
    b: Point
    length: int


@dataclass
class Day23PartBSolver:
    map: Mapping[Point, str]

    @property
    def solution(self) -> int:
        return max(self.get_lengths(self.start, set(), 0))

    def get_lengths(self, point: Point, seen: set[Point], so_far: int) -> Iterator[int]:
        if point == self.goal:
            yield so_far
            return

        seen.add(point)
        segments = self.segments_by_start[point]
        next_segments = {s for s in segments if s.b not in seen}
        for segment in next_segments:
            yield from self.get_lengths(segment.b, seen, so_far + segment.length)
        seen.remove(point)

    def next_points(self, point: Point) -> set[Point]:
        return {n for n in point.neighbors}

    @cached_property
    def junctions(self) -> set[Point]:
        output = set[Point]()
        points = {p for p in self.map.keys() if self.is_walkable(p)}
        for point in points:
            available = {p for p in point.neighbors if self.is_walkable(p)}
            if len(available) > 2:
                output.add(point)
        return output

    @cached_property
    def nodes(self) -> set[Point]:
        return self.junctions | {self.start, self.goal}

    @cached_property
    def segments_by_start(self) -> Mapping[Point, set[Segment]]:
        output = dict[Point, set[Segment]]()
        for segment in self.segments:
            if segment.a not in output:
                output[segment.a] = set()
            output[segment.a].add(segment)
        return output

    @cached_property
    def segments(self) -> set[Segment]:
        output = set[Segment]()
        for junction in self.junctions:
            for segment in self.get_segments_from_junction(junction):
                output.add(segment)
        return output

    def get_segments_from_junction(self, junction: Point) -> Iterator[Segment]:
        neighbors = [p for p in junction.neighbors if self.is_walkable(p)]
        for p in neighbors:
            yield from self.get_segments_from_point(junction, p, {junction})

    def get_segments_from_point(
        self, start: Point, current: Point, seen: set[Point]
    ) -> Iterator[Segment]:
        if current in self.nodes:
            yield Segment(start, current, len(seen))
            yield Segment(current, start, len(seen))
            return

        seen.add(current)
        next_points = [
            p for p in current.neighbors if self.is_walkable(p) and p not in seen
        ]
        yield from self.get_segments_from_point(start, next_points[0], seen)
        seen.remove(current)

    def is_walkable(self, point: Point) -> bool:
        return self.map.get(point, "#") != "#"

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
    solver = Day23PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_23/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

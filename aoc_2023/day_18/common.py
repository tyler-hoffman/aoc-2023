from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property

from aoc_2023.tools.point import Point


@dataclass
class Instruction:
    direction: str
    length: int
    color: str


@dataclass(frozen=True)
class VerticalSegment:
    x: int
    y_range: tuple[int, int]

    def __post_init__(self):
        assert self.y_range[0] < self.y_range[1]


UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

INSTRUCTION_MAP = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT,
}


@dataclass
class Solver:
    instructions: list[Instruction]

    @cached_property
    def solution(self) -> int:
        by_y = self.segments_by_y_range
        terminals = set[VerticalSegment]()
        output = 0

        for x in self.xs:
            for segment in self.segments_by_x[x]:
                if segment not in terminals:
                    index_by_y = by_y[segment.y_range].index(segment)
                    end_segment = by_y[segment.y_range][index_by_y + 1]
                    width = (end_segment.x + 1) - segment.x
                    assert width > 0
                    height = segment.y_range[1] - segment.y_range[0]
                    assert height > 0
                    output += width * height
                    terminals.add(end_segment)

        output += self.left_len
        return output + 1

    @cached_property
    def xs(self) -> list[int]:
        return sorted({p.x for p in self.points})

    @cached_property
    def ys(self) -> list[int]:
        return sorted({p.y for p in self.points})

    @cached_property
    def points(self) -> list[Point]:
        pos = Point(0, 0)
        output = [pos]
        for inst in self.instructions:
            move = INSTRUCTION_MAP[inst.direction].multiply(inst.length)
            pos = pos.add(move)
            output.append(pos)
        return output

    @cached_property
    def segments_by_x(self) -> dict[int, list[VerticalSegment]]:
        output = dict[int, list[VerticalSegment]]()
        for segment in self.small_vertical_segments:
            if segment.x not in output:
                output[segment.x] = []
            output[segment.x].append(segment)
        for segments in output.values():
            segments.sort(key=lambda s: s.y_range)
        return output

    @cached_property
    def segments_by_y_range(self) -> dict[tuple[int, int], list[VerticalSegment]]:
        output = dict[tuple[int, int], list[VerticalSegment]]()
        for segment in self.small_vertical_segments:
            if segment.y_range not in output:
                output[segment.y_range] = []
            output[segment.y_range].append(segment)
        for segments in output.values():
            segments.sort(key=lambda s: s.x)
        return output

    @cached_property
    def small_vertical_segments(self) -> list[VerticalSegment]:
        output = list[VerticalSegment]()
        for large_segment in self.large_vertical_segments:
            ys = [
                y
                for y in self.ys
                if y >= large_segment.y_range[0] and y <= large_segment.y_range[1]
            ]
            for i in range(1, len(ys)):
                output.append(
                    VerticalSegment(
                        x=large_segment.x,
                        y_range=(ys[i - 1], ys[i]),
                    )
                )

        return output

    @cached_property
    def large_vertical_segments(self) -> list[VerticalSegment]:
        pos = Point(0, 0)
        output = list[VerticalSegment]()
        for inst in self.instructions:
            move = INSTRUCTION_MAP[inst.direction].multiply(inst.length)
            new_pos = pos.add(move)
            if new_pos.x == pos.x:
                output.append(
                    VerticalSegment(
                        x=new_pos.x,
                        y_range=(pos.y, new_pos.y)
                        if pos.y < new_pos.y
                        else (new_pos.y, pos.y),
                    )
                )
            pos = new_pos
        return output

    @cached_property
    def left_len(self) -> int:
        return sum(inst.length for inst in self.instructions if inst.direction == "L")

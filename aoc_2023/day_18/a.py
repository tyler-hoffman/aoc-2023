from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_18.common import DOWN, INSTRUCTION_MAP, RIGHT, Instruction
from aoc_2023.day_18.parser import Parser
from aoc_2023.tools.point import Point


@dataclass
class Day18PartASolver:
    instructions: list[Instruction]

    @property
    def solution(self) -> int:
        return len(self.all_holes)

    def print_me(self) -> None:
        holes = set(self.holes_dug)
        rows = list[str]()
        for y in range(self.min_y, self.max_y + 1):
            row = list[str]()
            for x in range(self.min_x, self.max_x + 1):
                row.append("#" if Point(x, y) in holes else ".")
            rows.append("".join(row))
        print()
        print("\n".join(rows))
        print()

    @cached_property
    def all_holes(self) -> set[Point]:
        output = set(self.holes_dug)
        start = self.holes_dug[0]
        assert start.add(RIGHT) in output
        assert start.add(DOWN) in output

        to_expand = [start.add(RIGHT).add(DOWN)]
        output.add(to_expand[0])

        while to_expand:
            point = to_expand.pop()
            output.add(point)
            for p in point.neighbors:
                if p not in output:
                    output.add(p)
                    to_expand.append(p)

        return output

    @cached_property
    def holes_dug(self) -> list[Point]:
        pos = Point(0, 0)
        output = [pos]

        for instruction in self.instructions:
            for _ in range(instruction.length):
                pos = pos.add(INSTRUCTION_MAP[instruction.direction])
                output.append(pos)

        return output

    @cached_property
    def min_x(self) -> int:
        return min(p.x for p in self.holes_dug)

    @cached_property
    def max_x(self) -> int:
        return max(p.x for p in self.holes_dug)

    @cached_property
    def min_y(self) -> int:
        return min(p.y for p in self.holes_dug)

    @cached_property
    def max_y(self) -> int:
        return max(p.y for p in self.holes_dug)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day18PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_18/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

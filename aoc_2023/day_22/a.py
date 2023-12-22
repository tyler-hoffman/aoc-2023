from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_22.common import Brick
from aoc_2023.day_22.parser import Parser


@dataclass
class Day22PartASolver:
    bricks: list[Brick]

    @property
    def solution(self) -> int:
        support_map = self.support_map
        support_count: dict[Brick, int] = {b: 0 for b in self.stacked}
        for supported in support_map.values():
            for brick in supported:
                support_count[brick] += 1

        to_disintigrate = set[Brick]()
        for brick, supports in support_map.items():
            if not any([b for b in supports if support_count[b] == 1]):
                to_disintigrate.add(brick)

        return len(to_disintigrate)

    @cached_property
    def support_map(self) -> Mapping[Brick, set[Brick]]:
        output: dict[Brick, set[Brick]] = {b: set() for b in self.stacked}
        zs = sorted({b.start.z for b in self.stacked})

        by_z: dict[int, set[Brick]] = {z: set() for z in zs}
        for brick in self.stacked:
            by_z[brick.start.z].add(brick)

        for brick in self.stacked:
            z_above = brick.end.z + 1
            if z_above in by_z:
                for other in by_z[z_above]:
                    if brick.overlaps(other):
                        output[brick].add(other)
            else:
                assert brick.start.z == max(zs)

        return output

    @cached_property
    def stacked(self) -> list[Brick]:
        output = list[Brick]()

        for brick in self.sorted_vertically:
            found_it = False
            for i in range(len(output) - 1, -1, -1):
                other = output[i]
                if brick.overlaps(other):
                    found_it = True
                    output.append(brick.drop(other.end.z + 1))
                    break
            if not found_it:
                output.append(brick.drop(1))
            # TODO: buble-sort the last item down would be faster
            output.sort(key=lambda b: (b.end.z, b.start.y, b.start.x))

        return output

    @cached_property
    def sorted_vertically(self) -> list[Brick]:
        return sorted(
            self.bricks,
            key=lambda b: (b.start.z, b.start.y, b.start.x),
        )


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day22PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

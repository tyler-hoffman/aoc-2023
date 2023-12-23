from collections.abc import Mapping
from dataclasses import dataclass, field
from functools import cache, cached_property
from aoc_2023.day_22.common import Brick
from aoc_2023.day_22.parser import Parser


@dataclass(frozen=True)
class Day22PartBSolver:
    bricks: list[Brick] = field(hash=False)

    @property
    def solution(self) -> int:
        fall_counts = [self.fall_count(b) for b in self.stacked]
        return sum(fall_counts)

    @cache
    def fall_count(self, to_remove: Brick) -> int:
        nuked = {to_remove}
        for z, bricks in self.bricks_at_level.items():
            if z <= to_remove.start.z:
                continue
            for brick in bricks:
                if all(b in nuked for b in self.supported_by_map[brick]):
                    nuked.add(brick)
        return len(nuked) - 1

    @cached_property
    def supported_by_map(self) -> Mapping[Brick, set[Brick]]:
        output: dict[Brick, set[Brick]] = {b: set() for b in self.stacked}
        for brick, supports in self.support_map.items():
            for b in supports:
                output[b].add(brick)
        return output

    @cached_property
    def support_map(self) -> Mapping[Brick, set[Brick]]:
        output: dict[Brick, set[Brick]] = {b: set() for b in self.stacked}
        for brick in self.stacked:
            z_above = brick.end.z + 1
            for other in self.bricks_at_level.get(z_above, set()):
                if brick.overlaps(other):
                    output[brick].add(other)
        return output

    @cached_property
    def bricks_at_level(self) -> Mapping[int, set[Brick]]:
        zs = sorted({b.start.z for b in self.stacked})
        by_z: dict[int, set[Brick]] = {z: set() for z in zs}
        for brick in self.stacked:
            by_z[brick.start.z].add(brick)
        return by_z

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
    solver = Day22PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_22/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from functools import cached_property
from typing import Optional


@dataclass(frozen=True)
class MapSolver:
    id: int
    land_map: list[list[str]]
    smudges: int = 0

    @cached_property
    def score(self) -> int:
        assert None in (self.horizontal_reflection_line, self.vertical_reflection_line)
        if self.horizontal_reflection_line is not None:
            return 100 * (self.horizontal_reflection_line + 1)
        elif self.vertical_reflection_line is not None:
            return self.vertical_reflection_line + 1
        else:
            assert False

    @cached_property
    def horizontal_reflection_line(self) -> Optional[int]:
        return self.find_reflection_point(self.land_map)

    @cached_property
    def vertical_reflection_line(self) -> Optional[int]:
        return self.find_reflection_point(self.transposed_land_map)

    def find_reflection_point(self, land_map: list[list[str]]) -> Optional[int]:
        for i in range(0, len(land_map) - 1):
            if self.is_reflection_point(land_map, i):
                return i
        return None

    def is_reflection_point(
        self,
        land_map: list[list[str]],
        point: int,
    ) -> Optional[int]:
        diff_count = 0
        for diff in range(len(land_map)):
            y1 = point - diff
            y2 = point + 1 + diff

            if y1 < 0 or y2 >= len(land_map):
                break

            for x in range(len(land_map[0])):
                if land_map[y1][x] != land_map[y2][x]:
                    diff_count += 1
                    if diff_count > self.smudges:
                        return False

        return diff_count == self.smudges

    @cached_property
    def transposed_land_map(self) -> list[list[str]]:
        output = list[list[str]]()
        for x in range(self.width):
            output.append([])
            for y in range(self.height):
                output[-1].append(self.land_map[y][x])
        return output

    @cached_property
    def width(self) -> int:
        return len(self.land_map[0])

    @cached_property
    def height(self) -> int:
        return len(self.land_map)

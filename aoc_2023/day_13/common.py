from dataclasses import dataclass
from functools import cached_property
from typing import Optional


@dataclass(frozen=True)
class MapSolver:
    land_map: list[list[str]]

    @cached_property
    def score(self) -> int:
        assert None in (self.horizontal_reflection_line, self.vertical_reflection_line)
        if self.horizontal_reflection_line:
            return self.horizontal_reflection_line
        else:
            assert self.vertical_reflection_line
            return 100 * self.vertical_reflection_line

    @cached_property
    def horizontal_reflection_line(self) -> Optional[int]:
        ...

    @cached_property
    def vertical_reflection_line(self) -> Optional[int]:
        ...

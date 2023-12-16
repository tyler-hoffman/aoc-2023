from dataclasses import dataclass
from functools import cached_property


@dataclass
class Grid:
    chars: list[str]

    @cached_property
    def width(self) -> int:
        return len(self.chars[0])

    @cached_property
    def height(self) -> int:
        return len(self.chars)

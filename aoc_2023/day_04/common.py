from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Card:
    id: int
    winning_numbers: list[int]
    actual_numbers: list[int]

    @cached_property
    def matches(self) -> int:
        return len(set(self.winning_numbers) & set(self.actual_numbers))

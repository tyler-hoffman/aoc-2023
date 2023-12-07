from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from functools import cached_property, total_ordering

from aoc_2023.tools.freq_map import frequency_map

CARD_FACES = [str(x) for x in ["A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2]]
CARD_FACE_TO_VALUE = {c: i + 2 for i, c in enumerate(reversed(CARD_FACES))}

CARD_FACE_TO_VALUE = {
    c: 1 if c == "J" else i + 2 for i, c in enumerate(reversed(CARD_FACES))
}


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


@total_ordering
@dataclass(frozen=True)
class Hand:
    card_string: str
    bid: int

    @cached_property
    def card_freqs(self) -> defaultdict[str, int]:
        return frequency_map(self.card_string)

    def __lt__(self, other: Hand) -> bool:
        return self.type_and_values < other.type_and_values

    @cached_property
    def type_and_values(self) -> tuple[int, ...]:
        return tuple(
            [self.type.value, *[CARD_FACE_TO_VALUE[c] for c in self.card_string]]
        )

    @cached_property
    def type(self) -> HandType:
        non_jokers = [c for c in self.card_string if c != "J"]
        joker_count = len(self.card_string) - len(non_jokers)
        matches = sorted(frequency_map(non_jokers).values(), reverse=True)
        if matches:
            matches[0] += joker_count
        if joker_count == len(self.card_string):
            return HandType.FIVE_OF_A_KIND
        elif matches[0] == 5:
            return HandType.FIVE_OF_A_KIND
        elif matches[0] == 4:
            return HandType.FOUR_OF_A_KIND
        elif matches[0] == 3 and matches[1] == 2:
            return HandType.FULL_HOUSE
        elif matches[0] == 3:
            return HandType.THREE_OF_A_KIND
        elif matches[0] == 2 and matches[1] == 2:
            return HandType.TWO_PAIR
        elif matches[0] == 2:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

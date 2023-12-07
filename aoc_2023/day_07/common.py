from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from functools import cache


CARD_FACES = [str(x) for x in ["A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2]]
CARD_FACE_TO_VALUE = {c: i + 2 for i, c in enumerate(reversed(CARD_FACES))}

CARD_FACE_TO_VALUE_JOKER_EDITION = {
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


@dataclass(frozen=True)
class Hand:
    card_string: str
    bid: int


@dataclass(frozen=True)
class Game(ABC):
    hands: tuple[Hand, ...]

    @property
    def score(self) -> int:
        sorted_hands = sorted(
            self.hands, key=lambda hand: self.hand_type_and_values(hand)
        )
        pairs = [(hand.bid, i + 1) for i, hand in enumerate(sorted_hands)]
        return sum(a * b for a, b in pairs)

    @cache
    def hand_type_and_values(self, hand: Hand) -> tuple[int, ...]:
        return tuple(
            [
                self.hand_type(hand).value,
                *[self.card_face_to_value[c] for c in hand.card_string],
            ]
        )

    @property
    @abstractmethod
    def card_face_to_value(self) -> dict[str, int]:
        ...

    @abstractmethod
    def hand_type(self, hand: Hand) -> HandType:
        ...

    def hand_type_for_card_frequency(self, card_freq_map: dict[str, int]) -> HandType:
        matches = sorted(card_freq_map.values(), reverse=True)
        if matches[0] == 5:
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

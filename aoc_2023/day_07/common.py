from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


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

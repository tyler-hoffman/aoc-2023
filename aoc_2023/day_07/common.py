from dataclasses import dataclass


@dataclass
class Hand:
    card_string: str
    bid: int

from dataclasses import dataclass
from functools import cache
from aoc_2023.day_07.common import (
    CARD_FACE_TO_VALUE,
    Hand,
    HandType,
)
from aoc_2023.day_07.parser import Parser
from aoc_2023.tools.freq_map import frequency_map


@dataclass(frozen=True)
class Day07PartASolver:
    hands: tuple[Hand, ...]

    @property
    def solution(self) -> int:
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
                *[CARD_FACE_TO_VALUE[c] for c in hand.card_string],
            ]
        )

    @cache
    def hand_type(self, hand: Hand) -> HandType:
        matches = sorted(frequency_map(hand.card_string).values(), reverse=True)
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


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartASolver(tuple(data))

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

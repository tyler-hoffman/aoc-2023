from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_07.common import (
    CARD_FACE_TO_VALUE,
    Game,
    Hand,
    HandType,
)
from aoc_2023.day_07.parser import Parser
from aoc_2023.tools.freq_map import frequency_map


class PartAGame(Game):
    @cached_property
    def card_face_to_value(self) -> dict[str, int]:
        return CARD_FACE_TO_VALUE

    def hand_type(self, hand: Hand) -> HandType:
        freqs = frequency_map(hand.card_string)
        return self.hand_type_for_card_frequency(freqs)


@dataclass(frozen=True)
class Day07PartASolver:
    hands: tuple[Hand, ...]

    @property
    def solution(self) -> int:
        return PartAGame(self.hands).score


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

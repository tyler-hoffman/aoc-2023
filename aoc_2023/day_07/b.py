from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_07.common import (
    CARD_FACE_TO_VALUE_JOKER_EDITION,
    Game,
    Hand,
    HandType,
)
from aoc_2023.day_07.parser import Parser
from aoc_2023.tools.freq_map import frequency_map


class PartBGame(Game):
    @cached_property
    def card_face_to_value(self) -> dict[str, int]:
        return CARD_FACE_TO_VALUE_JOKER_EDITION

    def hand_type(self, hand: Hand) -> HandType:
        non_jokers = [c for c in hand.card_string if c != "J"]
        joker_count = len(hand.card_string) - len(non_jokers)
        matches = sorted(frequency_map(non_jokers).values(), reverse=True)
        if matches:
            matches[0] += joker_count
        if joker_count == len(hand.card_string):
            return HandType.FIVE_OF_A_KIND
        else:
            freqs = frequency_map(non_jokers)
            max_count = max(freqs.values())
            max_card = next(c for c, count in freqs.items() if count == max_count)
            freqs[max_card] += joker_count
            return self.hand_type_for_card_frequency(freqs)


@dataclass(frozen=True)
class Day07PartBSolver:
    hands: tuple[Hand, ...]

    @property
    def solution(self) -> int:
        return PartBGame(self.hands).score


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartBSolver(tuple(data))

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

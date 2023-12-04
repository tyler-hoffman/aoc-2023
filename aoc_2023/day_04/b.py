from dataclasses import dataclass
from functools import cached_property
from typing import Mapping, Sequence
from aoc_2023.day_04.common import Card
from aoc_2023.day_04.parser import Parser


@dataclass
class Day04PartBSolver:
    cards: list[Card]

    @property
    def solution(self) -> int:
        card_freqs = {card.id: 1 for card in self.cards}

        for id in self.card_ids:
            card = self.cards_by_id[id]
            for i in range(card.matches):
                card_freqs[id + 1 + i] += card_freqs[id]

        return sum(freq for freq in card_freqs.values())

    @cached_property
    def card_count(self) -> int:
        return len(self.cards)

    @cached_property
    def cards_by_id(self) -> Mapping[int, Card]:
        return {card.id: card for card in self.cards}

    @cached_property
    def card_ids(self) -> Sequence[int]:
        return list(range(1, self.card_count))


def solve(input: str) -> int:
    cards = Parser.parse(input)
    solver = Day04PartBSolver(cards)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

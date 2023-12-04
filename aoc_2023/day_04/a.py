from dataclasses import dataclass
from aoc_2023.day_04.common import Card
from aoc_2023.day_04.parser import Parser


@dataclass
class Day04PartASolver:
    cards: list[Card]

    @property
    def solution(self) -> int:
        return sum(self.points(card) for card in self.cards)

    def points(self, card: Card) -> int:
        matches = card.matches
        if matches == 0:
            return 0
        else:
            return 2 ** (matches - 1)


def solve(input: str) -> int:
    cards = Parser.parse(input)
    solver = Day04PartASolver(cards)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_04/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from dataclasses import dataclass
from aoc_2023.day_07.common import Hand
from aoc_2023.day_07.parser import Parser


@dataclass
class Day07PartASolver:
    hands: list[Hand]

    @property
    def solution(self) -> int:
        sorted_hands = sorted(self.hands)
        pairs = [(hand.bid, i + 1) for i, hand in enumerate(sorted_hands)]
        return sum(a * b for a, b in pairs)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day07PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_07/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

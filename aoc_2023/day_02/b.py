from dataclasses import dataclass
from aoc_2023.day_02.common import Game
from aoc_2023.day_02.parser import Parser


@dataclass
class Day02PartBSolver:
    games: list[Game]

    @property
    def solution(self) -> int:
        return sum([self.min_power(g) for g in self.games])

    def min_power(self, game: Game) -> int:
        r = max(c.red for c in game.color_sets)
        g = max(c.green for c in game.color_sets)
        b = max(c.blue for c in game.color_sets)

        return r * g * b


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day02PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

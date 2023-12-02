from dataclasses import dataclass
from aoc_2023.day_02.common import ColorSet, Game
from aoc_2023.day_02.parser import Parser


@dataclass
class Day02PartASolver:
    games: list[Game]
    target_color_set: ColorSet

    @property
    def solution(self) -> int:
        possible_games = [g for g in self.games if self.is_possible(g)]
        return sum(g.id for g in possible_games)

    def is_possible(self, game: Game) -> bool:
        for color_set in game.color_sets:
            if any(
                [
                    color_set.red > self.target_color_set.red,
                    color_set.green > self.target_color_set.green,
                    color_set.blue > self.target_color_set.blue,
                ]
            ):
                return False
        return True


def solve(input: str) -> int:
    data = Parser.parse(input)
    color_set = ColorSet(red=12, green=13, blue=14)
    solver = Day02PartASolver(data, color_set)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

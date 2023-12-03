from dataclasses import dataclass
from functools import cached_property
from aoc_2023.day_03.common import Analyzer, Value
from aoc_2023.day_03.parser import Parser


@dataclass
class Day03PartBSolver:
    lines: list[str]

    @property
    def solution(self) -> int:
        gears = {
            star: list(part_numbers)
            for star, part_numbers in self.stars_to_part_numbers.items()
            if len(part_numbers) == 2
        }

        products = [int(pn[0].value) * int(pn[1].value) for pn in gears.values()]
        return sum(products)

    @cached_property
    def stars_to_part_numbers(self) -> dict[Value, set[Value]]:
        star_to_part_numbers: dict[Value, set[Value]] = {
            star: set() for star in self.analyzer.stars
        }
        for star in self.analyzer.stars:
            for number in self.analyzer.part_numbers:
                bounds = self.analyzer.bounding_box(number)
                if bounds.contains(star.start, star.line_number):
                    star_to_part_numbers[star].add(number)
        return star_to_part_numbers

    @cached_property
    def analyzer(self) -> Analyzer:
        return Analyzer(self.lines)


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day03PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_03/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

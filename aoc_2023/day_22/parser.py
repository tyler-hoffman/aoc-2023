import string
from aoc_2023.day_22.common import Brick, Point

LETTERS = string.ascii_lowercase


class Parser:
    @staticmethod
    def parse(input: str) -> list[Brick]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line, i) for i, line in enumerate(lines)]

    @staticmethod
    def parse_line(line: str, i: int) -> Brick:
        start, end = line.split("~")
        starts = (int(x) for x in start.split(","))
        ends = (int(x) for x in end.split(","))

        name = LETTERS[i] if i < len(LETTERS) else None

        return Brick(Point(*starts), Point(*ends), name)

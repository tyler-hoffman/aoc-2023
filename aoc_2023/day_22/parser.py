from aoc_2023.day_22.common import Brick, Point


class Parser:
    @staticmethod
    def parse(input: str) -> list[Brick]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Brick:
        start, end = line.split("~")
        starts = (int(x) for x in start.split(","))
        ends = (int(x) for x in end.split(","))

        return Brick(Point(*starts), Point(*ends))

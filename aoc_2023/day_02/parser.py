from aoc_2023.day_02.common import Game, ColorSet


class Parser:
    @staticmethod
    def parse(input: str) -> list[Game]:
        lines = input.strip().splitlines()
        return [Parser.parse_game(line) for line in lines]

    @staticmethod
    def parse_game(input: str) -> Game:
        start, rest = input.split(": ")
        id = start.split(" ")[1]
        color_set = rest.split("; ")

        return Game(
            id=int(id),
            color_sets=[Parser.parse_color_set(c) for c in color_set],
        )

    @staticmethod
    def parse_color_set(input: str) -> ColorSet:
        parts = input.split(", ")
        r = 0
        g = 0
        b = 0

        for part in parts:
            count, label = part.split(" ")
            num = int(count)

            match label:
                case "red":
                    r = num
                case "green":
                    g = num
                case "blue":
                    b = num
                case _:
                    assert False

        return ColorSet(red=r, green=g, blue=b)

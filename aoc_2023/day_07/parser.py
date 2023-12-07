from aoc_2023.day_07.common import Hand


class Parser:
    @staticmethod
    def parse(input: str) -> list[Hand]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Hand:
        cards, bid = line.split()
        return Hand(cards, int(bid))

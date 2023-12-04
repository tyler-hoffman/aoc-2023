from aoc_2023.day_04.common import Card


class Parser:
    @staticmethod
    def parse(input: str) -> list[Card]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Card:
        first, second = line.split(":")
        _, id = first.split()
        winning_list, actual_list = second.split("|")
        winning = winning_list.strip().split()
        actual = actual_list.strip().split()

        return Card(
            id=int(id),
            winning_numbers=[int(x) for x in winning],
            actual_numbers=[int(x) for x in actual],
        )

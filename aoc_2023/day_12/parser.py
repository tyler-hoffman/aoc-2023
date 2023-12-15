from aoc_2023.day_12.common import Record


class Parser:
    @staticmethod
    def parse(input: str) -> list[Record]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Record:
        chars, congruencies = line.split()
        return Record(
            chars=chars, congruencies=[int(x) for x in congruencies.split(",")]
        )

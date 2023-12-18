from aoc_2023.day_18.common import Instruction


class Parser:
    @staticmethod
    def parse(input: str) -> list[Instruction]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Instruction:
        direction, length, color = line.split()

        return Instruction(direction, int(length), color[2:-1])

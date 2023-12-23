from typing import Mapping
from aoc_2023.tools.point import Point


class Parser:
    @staticmethod
    def parse(input: str) -> Mapping[Point, str]:
        output = dict[Point, str]()
        lines = input.strip().splitlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                output[Point(x, y)] = char
        return output

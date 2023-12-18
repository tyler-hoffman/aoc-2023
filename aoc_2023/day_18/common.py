from dataclasses import dataclass

from aoc_2023.tools.point import Point


@dataclass
class Instruction:
    direction: str
    length: int
    color: str


UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

INSTRUCTION_MAP = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT,
}

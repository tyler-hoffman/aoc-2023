from dataclasses import dataclass


@dataclass
class Instruction:
    direction: str
    length: int
    color: str

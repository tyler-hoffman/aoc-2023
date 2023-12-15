from dataclasses import dataclass


def hash_it(line: str) -> int:
    output = 0
    for char in line:
        output += ord(char)
        output *= 17
        output %= 256
    return output


@dataclass
class Minus:
    label: str


@dataclass
class Equal:
    label: str
    val: int

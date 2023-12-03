from dataclasses import dataclass


@dataclass(frozen=True)
class Value:
    value: int
    line_number: int
    start: int
    end: int

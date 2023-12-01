from dataclasses import dataclass
from typing import Mapping, Sequence


@dataclass
class Day01Solver:
    lines: Sequence[str]
    num_map: Mapping[str, int]

    @property
    def solution(self) -> int:
        return sum(self.line_values)

    @property
    def line_values(self) -> list[int]:
        firsts_and_lasts = [self.first_and_last(line) for line in self.lines]
        return [int(f"{a}{b}") for a, b in firsts_and_lasts]

    def first_and_last(self, line: str) -> tuple[int, int]:
        indexes = list(range(len(line)))
        first = self.first_instance(line, indexes)
        last = self.first_instance(line, indexes[::-1])

        return first, last

    def first_instance(self, line: str, indexes: list[int]) -> int:
        for i in indexes:
            for string, value in self.num_map.items():
                if line[i:].startswith(string):
                    return value
        assert False, "we shouldn't get here"

from dataclasses import dataclass
from typing import Iterator, Optional
from aoc_2023.day_12.common import Record
from aoc_2023.day_12.parser import Parser


@dataclass
class Day12PartASolver:
    records: list[Record]

    @property
    def solution(self) -> int:
        output = 0
        for record in self.records:
            output += len(list(self.get_variations(record.chars[:], record)))
        return output

    @staticmethod
    def is_valid_sequence(seq: list[str], record: Record) -> bool:
        return Day12PartASolver.get_congruencies(seq) == record.congruencies

    @staticmethod
    def get_congruencies(seq: list[str], length: Optional[int] = None) -> list[int]:
        end = length if length is not None else len(seq)
        congruencies = list[int]()
        count = 0
        prev = "."
        for i, ch in enumerate(seq):
            if i >= end:
                break
            if ch == "." and prev == "#":
                if count:
                    congruencies.append(count)
                count = 0
            if ch == "#":
                count += 1
            prev = ch
        if count:
            congruencies.append(count)
        return congruencies

    def get_variations(
        self, chars: list[str], record: Record, index: int = 0
    ) -> Iterator[list[str]]:
        congruencies = self.get_congruencies(chars[:index])
        if congruencies[:-1] != record.congruencies[: len(congruencies)][:-1]:
            return
        if index == len(chars):
            if self.is_valid_sequence(chars, record):
                yield chars[:]
        else:
            match chars[index]:
                case ".":
                    yield from self.get_variations(chars, record, index + 1)
                case "#":
                    yield from self.get_variations(chars, record, index + 1)
                case "?":
                    chars[index] = "."
                    yield from self.get_variations(chars, record, index + 1)
                    chars[index] = "#"
                    yield from self.get_variations(chars, record, index + 1)
                    chars[index] = "?"
                case _:
                    assert False


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day12PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_12/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property


@dataclass(frozen=True)
class Record:
    chars: list[str]
    congruencies: list[int]


period_pattern = re.compile(r"\.+")


@dataclass(frozen=True)
class Day12Solver(ABC):
    @property
    @abstractmethod
    def records(self) -> list[Record]:
        ...

    @property
    def solution(self) -> int:
        return sum(RecordSolver(r).variations for r in self.records)


@dataclass(frozen=True)
class RecordSolver:
    record: Record = field(hash=False)

    @cached_property
    def variations(self) -> int:
        return self.solve_it(
            chars=self.record.chars[:],
            congruencies=self.record.congruencies[:],
        )

    def solve_it(
        self,
        chars: list[str],
        congruencies: list[int],
    ) -> int:
        if len(congruencies) == 0:
            output = 1 if all(ch != "#" for ch in chars) else 0
            return output
        elif len(congruencies) == 1:
            return self.congruency_matches("".join(chars), congruencies[0])
        else:
            if len(chars) == 0:
                return 0
            mid = len(chars) // 2
            if chars[mid] == ".":
                return self.split_as_period(chars, congruencies)
            elif chars[mid] == "#":
                return self.split_as_hash(chars, congruencies)
            elif chars[mid] == "?":
                return self.split_as_period(chars, congruencies) + self.split_as_hash(
                    chars, congruencies
                )
            else:
                assert False

    def congruency_matches(self, chars: str, congruency: int) -> int:
        groups = period_pattern.split(chars)
        with_hashes = [g for g in groups if "#" in groups]
        match len(with_hashes):
            case 0:
                output = 0
                for group in groups:
                    if len(group) >= congruency:
                        return len(group) + 1 - congruency
                return output
            case 1:
                if len(with_hashes[0]) >= congruency:
                    return len(with_hashes[0]) + 1 - congruency
                else:
                    return 0
            case _:
                return 0

    def split_as_period(self, chars: list[str], congruencies: list[int]) -> int:
        mid = len(chars) // 2
        assert mid != "#"
        left_chars = chars[:mid]
        right_chars = chars[mid + 1 :]
        output = 0
        for i in range(len(congruencies)):
            output += self.solve_it(left_chars, congruencies[:i]) * self.solve_it(
                right_chars, congruencies[i:]
            )
        return output

    def split_as_hash(self, chars: list[str], congruencies: list[int]) -> int:
        output = 0
        mid = len(chars) // 2
        assert mid != "."
        output = 0
        for i in range(len(congruencies)):
            congruency = congruencies[i]
            for to_the_left in range(congruency):
                to_the_right = congruency - to_the_left
                output += self.solve_it(
                    chars[: mid - to_the_left], congruencies[:i]
                ) * self.solve_it(chars[mid + to_the_right :], congruencies[i + 1 :])
        return output

    def remove_surrounding_periods(self, string: str) -> str:
        return string.replace(".", " ").strip().replace(" ", ".")

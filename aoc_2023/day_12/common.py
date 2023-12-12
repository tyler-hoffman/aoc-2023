from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator, Optional


@dataclass(frozen=True)
class Record:
    chars: list[str]
    congruencies: list[int]


@dataclass(frozen=True)
class Day12Solver(ABC):
    @property
    @abstractmethod
    def records(self) -> list[Record]:
        ...

    @property
    def solution(self) -> int:
        # return sum(RecordSolver(r).variations for r in self.records)
        output = 0
        for record in self.records:
            output += len(list(self.get_variations(record.chars[:], record)))
        return output

    @staticmethod
    def is_valid_sequence(seq: list[str], record: Record) -> bool:
        return Day12Solver.get_congruencies(seq) == record.congruencies

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


@dataclass(frozen=True)
class RecordSolver:
    record: Record = field(hash=False)
    # char_index: int = field(default=0)
    # start_stack: list[int] = field(default_factory=list)

    @cached_property
    def current_chars(self) -> list[str]:
        return self.record.chars[:]

    @cached_property
    def variations(self) -> int:
        return len(
            list(
                self.solve_it(
                    char_index=0,
                    run_length=0,
                    congruencies_seen=0,
                    start_stack=[-1],
                )
            )
        )

    def solve_it(
        self,
        char_index: int,
        run_length: int,
        congruencies_seen: int,
        start_stack: list[int],
    ) -> Iterator[bool]:
        if char_index == len(self.record.chars):
            congruencies_left = len(self.record.congruencies) - congruencies_seen
            if (
                run_length
                and congruencies_left == 1
                and self.record.congruencies[-1] == run_length
            ):
                yield True
            elif run_length == 0 and congruencies_left == 0:
                yield True
            return
        else:
            match self.record.chars[char_index]:
                case ".":
                    if (
                        run_length
                        and run_length == self.record.congruencies[congruencies_seen]
                    ):
                        start_stack.append(char_index)
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=0,
                            congruencies_seen=congruencies_seen + 1,
                            start_stack=start_stack,
                        )
                        start_stack.pop()

                    elif not run_length:
                        start_stack.append(char_index)
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=0,
                            congruencies_seen=congruencies_seen,
                            start_stack=start_stack,
                        )
                        start_stack.pop()
                case "#":
                    new_run_length = run_length + 1
                    if (
                        congruencies_seen < len(self.record.congruencies)
                        and new_run_length
                        <= self.record.congruencies[congruencies_seen]
                    ):
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=new_run_length,
                            congruencies_seen=congruencies_seen,
                            start_stack=start_stack,
                        )

                case "?":
                    new_run_length = run_length + 1
                    if (
                        congruencies_seen < len(self.record.congruencies)
                        and new_run_length
                        <= self.record.congruencies[congruencies_seen]
                    ):
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=new_run_length,
                            congruencies_seen=congruencies_seen,
                            start_stack=start_stack,
                        )

                    if (
                        run_length
                        and run_length == self.record.congruencies[congruencies_seen]
                    ):
                        start_stack.append(char_index)
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=0,
                            congruencies_seen=congruencies_seen + 1,
                            start_stack=start_stack,
                        )
                        start_stack.pop()

                    elif not run_length:
                        start_stack.append(char_index)
                        yield from self.solve_it(
                            char_index=char_index + 1,
                            run_length=0,
                            congruencies_seen=congruencies_seen,
                            start_stack=start_stack,
                        )
                        start_stack.pop()
                case _:
                    assert False

    # @cached_property
    # def variations(self) -> int:
    #     subsequences = self._get_sub_sequences(self.record.chars)
    #     for subsequence in subsequences:
    #         for sub_variation in self.get_sub_variations(subsequence):

    #     return 0

    # def solve_it(self, subsequence_index:int, congruency_index: int) -> Iterator[bool]:
    #     if subsequence_index == len(self.subsequences) or congruency_index == len(self.record.congruencies):
    #         return

    #     for i, sub_variation in self.get_sub_variations(self.subsequences[sub_variation]):

    # def get_sub_variations(
    #     self,
    #     chars: list[str],
    #     index: int = 0,
    # ) -> Iterator[list[int]]:
    #     if index == len(chars):
    #         return
    #     congruencies = self.get_congruencies(chars[:index])
    #     if congruencies[:-1] != self.record.congruencies[: len(congruencies)][:-1]:
    #         if self.is_valid_sequence(chars, record):
    #             yield chars[:]

    #     output = list[int]()
    #     assert len(chars) > 0

    #     match chars[index]:
    #         case "#":
    #             yield from self.get_sub_variations(chars, index + 1)
    #         case "?":
    #             chars[index] = "."
    #             yield from self.get_sub_variations(chars, index + 1)
    #             chars[index] = "#"
    #             yield from self.get_sub_variations(chars, index + 1)
    #             chars[index] = "?"
    #         case _:
    #             assert False

    #     return output

    # @cached_property
    # def subsequences(self) -> list[list[str]]:
    #     return self._get_sub_sequences(self.record.chars)

    # def _get_sub_sequences(self, chars: list[str]) -> list[list[str]]:
    #     output = list[list[str]]()
    #     subseq = list[str]()
    #     for char in chars:
    #         if char == ".":
    #             if subseq:
    #                 output.append(subseq)
    #             subseq = []
    #         else:
    #             subseq.append(char)
    #     if subseq:
    #         output.append(subseq)
    #     return output

    # @staticmethod
    # def get_congruencies(seq: list[str], length: Optional[int] = None) -> list[int]:
    #     end = length if length is not None else len(seq)
    #     congruencies = list[int]()
    #     count = 0
    #     prev = "."
    #     for i, ch in enumerate(seq):
    #         if i >= end:
    #             break
    #         if ch == "." and prev == "#":
    #             if count:
    #                 congruencies.append(count)
    #             count = 0
    #         if ch == "#":
    #             count += 1
    #         prev = ch
    #     if count:
    #         congruencies.append(count)
    #     return congruencies

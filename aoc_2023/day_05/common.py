from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Range:
    start: int
    end: int

    def __post_init__(self) -> None:
        if not self.end > self.start:
            print(self)

    def shift(self, amt: int) -> Range:
        return Range(self.start + amt, self.end + amt)


@dataclass(frozen=True)
class Data:
    seeds: list[int]
    mapping_sets: list[MappingSet]


@dataclass(frozen=True)
class MappingSet:
    name: str
    mappings: list[Mapping]

    def map_value(self, value: int) -> int:
        in_range = [m for m in self.mappings if m.value_is_in_range(value)]
        match len(in_range):
            case 0:
                return value
            case 1:
                return value - in_range[0].diff
            case _:
                assert False

    def map_range(self, range: Range) -> set[Range]:
        to_check = [range]
        output = set[Range]()
        while len(to_check):
            range = to_check.pop()
            intersected = False
            for mapping in self.mappings:
                intersection = mapping.matching_range(range)
                if intersection is not None:
                    intersected = True
                    output.add(intersection.shift(-mapping.diff))
                    if range.start < intersection.start:
                        to_check.append(Range(range.start, intersection.start))
                    if intersection.end < range.end:
                        to_check.append(Range(intersection.end, range.end))
            if not intersected:
                output.add(range)

        return output


@dataclass(frozen=True)
class Mapping:
    destination: int
    source: int
    range: int

    def value_is_in_range(self, value: int) -> bool:
        return self.source <= value < self.source + self.range

    def matching_range(self, range: Range) -> Range | None:
        if range.start >= self.source_end or range.end <= self.source:
            return None
        else:
            start = max(range.start, self.source)
            end = min(range.end, self.source_end)

            return Range(start, end)

    @property
    def diff(self) -> int:
        return self.source - self.destination

    @property
    def source_end(self) -> int:
        return self.source + self.range

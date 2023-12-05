from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Data:
    seeds: list[int]
    mapping_sets: list[MappingSet]


@dataclass(frozen=True)
class MappingSet:
    name: str
    mappings: list[Mapping]

    def map(self, value: int) -> int:
        in_range = [m for m in self.mappings if m.value_is_in_range(value)]
        match len(in_range):
            case 0:
                return value
            case 1:
                return in_range[0].map(value)
            case _:
                assert False


@dataclass(frozen=True)
class Mapping:
    destination: int
    source: int
    range: int

    def map(self, value: int) -> int:
        if self.source <= value < self.source + self.range:
            return value - self.diff
        else:
            raise Exception("Woops")

    def value_is_in_range(self, value: int) -> bool:
        return self.source <= value < self.source + self.range

    @property
    def diff(self) -> int:
        return self.source - self.destination

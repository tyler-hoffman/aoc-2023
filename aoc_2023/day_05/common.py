from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Data:
    seeds: list[int]
    mapping_sets: list[MappingSet]


@dataclass
class MappingSet:
    name: str
    mappings: list[Mapping]


@dataclass
class Mapping:
    destination: int
    source: int
    range: int

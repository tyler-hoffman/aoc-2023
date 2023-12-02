from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Game:
    id: int
    color_sets: list[ColorSet]


@dataclass
class ColorSet:
    red: int = 0
    green: int = 0
    blue: int = 0

from dataclasses import dataclass


@dataclass(frozen=True)
class Race:
    time: int
    distance: int

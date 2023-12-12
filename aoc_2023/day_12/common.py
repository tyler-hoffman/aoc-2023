from dataclasses import dataclass


@dataclass(frozen=True)
class Record:
    chars: list[str]
    congruencies: list[int]

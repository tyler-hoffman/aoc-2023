from __future__ import annotations
import math
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Part:
    x: int
    m: int
    a: int
    s: int

    def val(self, label: str) -> int:
        return getattr(self, label)

    @property
    def score(self) -> int:
        return sum([self.x, self.m, self.a, self.s])


@dataclass
class Workflow:
    name: str
    rules: list[Predicate]


@dataclass
class Predicate(metaclass=ABCMeta):
    dest: str

    @abstractmethod
    def matches(self, part: Part) -> bool:
        ...


@dataclass
class LessThan(Predicate):
    dest: str
    field: str
    target: int

    def matches(self, part: Part) -> bool:
        return part.val(self.field) < self.target


@dataclass
class GreaterThan(Predicate):
    dest: str
    field: str
    target: int

    def matches(self, part: Part) -> bool:
        return part.val(self.field) > self.target


@dataclass
class Yes(Predicate):
    dest: str

    def matches(self, part: Part) -> bool:
        return True


@dataclass
class Data:
    workflows: list[Workflow]
    parts: list[Part]


@dataclass(frozen=True)
class NumRange:
    min: int = 1
    max: int = 4000

    @property
    def delta(self) -> int:
        return self.max + 1 - self.min


@dataclass(frozen=True)
class PartRange:
    x: NumRange = field(default_factory=NumRange)
    m: NumRange = field(default_factory=NumRange)
    a: NumRange = field(default_factory=NumRange)
    s: NumRange = field(default_factory=NumRange)

    def val(self, label: str) -> NumRange:
        return getattr(self, label)

    @property
    def is_valid(self) -> bool:
        return all([d > 0 for d in self.deltas])

    @property
    def score(self) -> int:
        return math.prod(self.deltas) if self.is_valid else 0

    @property
    def deltas(self) -> tuple[int, ...]:
        return tuple([r.delta for r in [self.x, self.m, self.a, self.s]])

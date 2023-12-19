from __future__ import annotations
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Part:
    x: int
    m: int
    a: int
    s: int

    def val(self, field: str) -> int:
        return getattr(self, field)

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

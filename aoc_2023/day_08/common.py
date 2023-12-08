from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    name: str
    left: str
    right: str


@dataclass(frozen=True)
class Data:
    directions: list[str]
    nodes: list[Node]

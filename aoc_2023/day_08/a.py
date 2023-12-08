from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_08.common import Data, Node
from aoc_2023.day_08.parser import Parser


@dataclass
class Day08PartASolver:
    data: Data

    @property
    def solution(self) -> int:
        dist = 0
        node = self.nodes_by_name["AAA"]
        while node.name != "ZZZ":
            direction = self.data.directions[dist % len(self.data.directions)]
            match direction:
                case "L":
                    node = self.nodes_by_name[node.left]
                case "R":
                    node = self.nodes_by_name[node.right]
                case _:
                    assert False
            dist += 1

        return dist

    @cached_property
    def nodes_by_name(self) -> Mapping[str, Node]:
        return {n.name: n for n in self.data.nodes}


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

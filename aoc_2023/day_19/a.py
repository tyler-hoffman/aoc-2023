from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_19.common import Data, Part, Workflow
from aoc_2023.day_19.parser import Parser


@dataclass
class Day19PartASolver:
    data: Data

    @property
    def solution(self) -> int:
        accepted = [p for p in self.parts if self.is_accepted(p)]
        return sum(p.score for p in accepted)

    def is_accepted(self, part: Part) -> bool:
        workflow_label = "in"
        while True:
            workflow = self.workflows[workflow_label]
            for rule in workflow.rules:
                if rule.matches(part):
                    match rule.dest:
                        case "A":
                            return True
                        case "R":
                            return False
                        case dest:
                            workflow_label = dest
                            break

    @cached_property
    def workflows(self) -> Mapping[str, Workflow]:
        return {w.name: w for w in self.data.workflows}

    @cached_property
    def parts(self) -> list[Part]:
        return self.data.parts


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day19PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

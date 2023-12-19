from dataclasses import dataclass, replace
from functools import cached_property
from typing import Mapping
from aoc_2023.day_19.common import (
    Data,
    GreaterThan,
    LessThan,
    Part,
    PartRange,
    Workflow,
    Yes,
)
from aoc_2023.day_19.parser import Parser


@dataclass
class Day19PartBSolver:
    data: Data

    @property
    def solution(self) -> int:
        return self.get_solutions("in", PartRange())

    def get_solutions(self, workflow_label: str, part_range: PartRange) -> int:
        if workflow_label == "A":
            return part_range.score
        elif workflow_label == "R":
            return 0
        workflow = self.workflows[workflow_label]
        output = 0

        for rule in workflow.rules:
            match rule:
                case LessThan(dest, field, target):
                    num_range = part_range.val(field)
                    accepted_num_range = replace(num_range, max=target - 1)
                    rejected_num_range = replace(num_range, min=target)
                    accepted = replace(part_range, **{field: accepted_num_range})
                    if accepted.is_valid:
                        output += self.get_solutions(dest, accepted)
                    part_range = replace(part_range, **{field: rejected_num_range})
                case GreaterThan(dest, field, target):
                    num_range = part_range.val(field)
                    accepted_num_range = replace(num_range, min=target + 1)
                    rejected_num_range = replace(num_range, max=target)
                    accepted = replace(part_range, **{field: accepted_num_range})
                    if accepted.is_valid:
                        output += self.get_solutions(dest, accepted)
                    part_range = replace(part_range, **{field: rejected_num_range})
                case Yes(dest):
                    output += self.get_solutions(dest, part_range)

        return output

    @cached_property
    def workflows(self) -> Mapping[str, Workflow]:
        return {w.name: w for w in self.data.workflows}

    @cached_property
    def parts(self) -> list[Part]:
        return self.data.parts


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day19PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_19/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

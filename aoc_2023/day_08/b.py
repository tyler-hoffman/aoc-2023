import math
from dataclasses import dataclass
from functools import cached_property
from typing import Mapping
from aoc_2023.day_08.common import Data, Node
from aoc_2023.day_08.parser import Parser


@dataclass
class CycleData:
    cycle_start: int
    cycle_length: int
    pre_cycle_z_dists: tuple[int, ...]
    in_cycle_z_dists: tuple[int, ...]

    def is_z(self, dist: int) -> bool:
        if dist in self.pre_cycle_z_dists:
            return True
        else:
            dist_in_cycle = (dist - self.cycle_start) % self.cycle_length
            return dist_in_cycle in self.in_cycle_z_dists


@dataclass
class Day08PartBSolver:
    data: Data

    @property
    def solution(self) -> int:
        nodes = self.starting_nodes
        cycle_datas = [self.get_cycle_data(n) for n in nodes]
        leader = cycle_datas[0]

        # check if we have a pre-cycle match; not expected!
        for dist in leader.pre_cycle_z_dists:
            if all([c.is_z(dist) for c in cycle_datas]):
                return dist

        dist = leader.cycle_start
        jump_size = leader.cycle_length
        while True:
            for delta in leader.in_cycle_z_dists:
                new_dist = dist + delta
                matches = tuple([c for c in cycle_datas if c.is_z(new_dist)])
                jump_size = math.prod([c.cycle_length for c in matches])
                if len(matches) == len(cycle_datas):
                    return new_dist
            dist += jump_size

        assert False

    @cached_property
    def nodes_by_name(self) -> Mapping[str, Node]:
        return {n.name: n for n in self.data.nodes}

    @cached_property
    def starting_nodes(self) -> set[Node]:
        return {n for n in self.data.nodes if n.name.endswith("A")}

    @cached_property
    def ending_nodes(self) -> set[Node]:
        return {n for n in self.data.nodes if n.name.endswith("Z")}

    def get_cycle_data(self, node: Node) -> CycleData:
        dist = 0
        history = dict[tuple[str, int], int]()
        while True:
            direction_index = dist % len(self.data.directions)
            key = node.name, direction_index
            if key in history:
                break

            history[key] = dist
            direction = self.data.directions[direction_index]
            match direction:
                case "L":
                    node = self.nodes_by_name[node.left]
                case "R":
                    node = self.nodes_by_name[node.right]
                case _:
                    assert False
            dist += 1

        direction_index = dist % len(self.data.directions)
        key = node.name, direction_index
        cycle_start = history[key]
        cycle_length = dist - cycle_start
        terminal_points = {k: v for k, v in history.items() if k[0].endswith("Z")}
        pre_cycle_z_dists = sorted(
            dist for dist in terminal_points.values() if dist < cycle_start
        )
        in_cycle_z_dists = sorted(
            dist - cycle_start
            for dist in terminal_points.values()
            if dist >= cycle_start
        )

        return CycleData(
            cycle_start=cycle_start,
            cycle_length=cycle_length,
            pre_cycle_z_dists=tuple(pre_cycle_z_dists),
            in_cycle_z_dists=tuple(in_cycle_z_dists),
        )


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day08PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_08/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

from __future__ import annotations
from dataclasses import dataclass
from functools import cached_property, total_ordering
from queue import PriorityQueue
from typing import Optional
from aoc_2023.tools.point import Point


UP = Point(0, -1)
DOWN = Point(0, 1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)

DIRECTIONS = {UP, DOWN, LEFT, RIGHT}


@total_ordering
@dataclass
class State:
    pos: Point
    total_heat_loss: int
    prev: Optional[State]

    def __lt__(self, other: State) -> bool:
        return self.heuristic < other.heuristic

    @property
    def heuristic(self) -> int:
        return self.total_heat_loss - self.pos.dist(Point(0, 0))

    @property
    def last_move(self) -> Optional[Point]:
        if self.prev is None:
            return None
        return self.pos.subtract(self.prev.pos)

    @property
    def last_direction(self) -> Optional[Point]:
        last_move = self.last_move
        match last_move:
            case None:
                return None
            case Point(0, y):
                return Point(0, y // abs(y))
            case Point(x, 0):
                return Point(x // abs(x), 0)
            case _:
                assert False


@dataclass
class Day17Solver:
    grid: list[list[int]]
    min_move: int
    max_move: int

    @property
    def solution(self) -> int:
        seen = set[tuple[Point, Point]]()
        queue = PriorityQueue[tuple[int, State]]()
        queue.put((self.goal.dist(self.start), State(self.start, 0, None)))
        while True:
            cost, state = queue.get()
            if state.pos == self.goal:
                assert cost == state.total_heat_loss
                return state.total_heat_loss

            for direction in DIRECTIONS:
                if direction == state.last_direction:
                    continue
                elif direction.multiply(-1) == state.last_direction:
                    continue

                new_total_heat_loss = state.total_heat_loss
                for i in range(1, self.max_move + 1):
                    p = state.pos.add(direction.multiply(i))
                    if not self.in_bounds(p):
                        continue
                    new_total_heat_loss += self.grid[p.y][p.x]
                    if i < self.min_move:
                        continue

                    seen_key = (state.pos, p)
                    if (seen_key) in seen:
                        continue
                    dist_to_goal = p.dist(self.goal)
                    new_cost = new_total_heat_loss + dist_to_goal

                    seen.add(seen_key)
                    queue.put((new_cost, State(p, new_total_heat_loss, state)))

    @cached_property
    def start(self) -> Point:
        return Point(0, 0)

    @cached_property
    def goal(self) -> Point:
        return Point(self.height - 1, self.width - 1)

    def in_bounds(self, point: Point) -> bool:
        return all(
            [
                point.x >= 0,
                point.y >= 0,
                point.x < self.width,
                point.y < self.height,
            ]
        )

    @cached_property
    def width(self) -> int:
        return len(self.grid[0])

    @cached_property
    def height(self) -> int:
        return len(self.grid)

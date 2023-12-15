from aoc_2023.day_15.a import Day15PartASolver, get_solution, solve
from aoc_2023.day_15.from_prompt import (
    HASH,
    HASH_HASHED,
    SAMPLE_DATA,
    SAMPLE_SOLUTION_A,
)


def test_hash():
    assert Day15PartASolver.hash(HASH) == HASH_HASHED


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_A


def test_my_solution():
    assert get_solution() == 517015

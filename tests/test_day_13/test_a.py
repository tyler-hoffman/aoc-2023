from aoc_2023.day_13.a import get_solution, solve
from aoc_2023.day_13.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_A


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_A


def test_my_solution():
    assert get_solution() == 34100

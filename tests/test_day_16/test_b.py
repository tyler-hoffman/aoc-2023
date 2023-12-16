from aoc_2023.day_16.b import get_solution, solve
from aoc_2023.day_16.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_B


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_B


def test_my_solution():
    assert get_solution() == 8754

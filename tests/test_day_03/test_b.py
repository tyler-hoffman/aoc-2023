from aoc_2023.day_03.b import get_solution, solve
from aoc_2023.day_03.from_prompt import SAMPLE_DATA


def test_solve():
    assert solve(SAMPLE_DATA) == 467835


def test_my_solution():
    assert get_solution() == 75220503

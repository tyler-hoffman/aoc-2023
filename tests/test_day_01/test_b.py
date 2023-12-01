from aoc_2023.day_01.b import get_solution, solve
from aoc_2023.day_01.from_prompt import UPDATED_SAMPLE_DATA


def test_solve():
    assert solve(UPDATED_SAMPLE_DATA) == 281


def test_my_solution():
    assert get_solution() == 53340

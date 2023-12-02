from aoc_2023.day_02.b import get_solution, solve
from aoc_2023.day_02.from_prompt import SAMPLE_DATA


def test_solve():
    assert solve(SAMPLE_DATA) == 2286


def test_my_solution():
    assert get_solution() == 54911

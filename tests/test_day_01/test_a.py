from aoc_2023.day_01.a import get_solution, solve
from aoc_2023.day_01.from_prompt import SAMPLE_DATA


def test_solve():
    assert solve(SAMPLE_DATA) == 142


def test_my_solution():
    assert get_solution() == 52974

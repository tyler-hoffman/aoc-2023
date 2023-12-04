from aoc_2023.day_04.a import get_solution, solve
from aoc_2023.day_04.from_prompt import SAMPLE_DATA, SAMPLE_DATA_POINTS


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_DATA_POINTS


def test_my_solution():
    assert get_solution() == 32609

import pytest

from aoc_2023.day_02.a import get_solution, solve
from aoc_2023.day_02.from_prompt import SAMPLE_DATA


def test_solve():
    assert solve(SAMPLE_DATA) == 8


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"

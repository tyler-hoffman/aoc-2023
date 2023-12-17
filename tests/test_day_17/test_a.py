import pytest

from aoc_2023.day_17.a import get_solution, solve
from aoc_2023.day_17.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"

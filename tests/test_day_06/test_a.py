import pytest

from aoc_2023.day_06.a import get_solution, solve
from aoc_2023.day_06.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION_A


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION_A


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"

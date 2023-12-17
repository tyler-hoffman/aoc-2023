import pytest

from aoc_2023.day_17.b import get_solution, solve
from aoc_2023.day_17.from_prompt import (
    OTHER_SAMPLE_DATA,
    OTHER_SAMPLE_SOLUTION,
    SAMPLE_DATA,
    SAMPLE_SOLUTION_B,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_DATA, SAMPLE_SOLUTION_B),
        (OTHER_SAMPLE_DATA, OTHER_SAMPLE_SOLUTION),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 1210

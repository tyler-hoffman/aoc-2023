import pytest

from aoc_2023.day_08.a import get_solution, solve
from aoc_2023.day_08.from_prompt import (
    SAMPLE_DATA_1,
    SAMPLE_DATA_2,
    SAMPLE_SOLUTION_1,
    SAMPLE_SOLUTION_2,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_DATA_1, SAMPLE_SOLUTION_1),
        (SAMPLE_DATA_2, SAMPLE_SOLUTION_2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 21389

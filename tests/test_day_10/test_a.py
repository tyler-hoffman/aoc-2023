import pytest

from aoc_2023.day_10.a import get_solution, solve
from aoc_2023.day_10.from_prompt import (
    SAMPLE_INPUT_1,
    SAMPLE_INPUT_2,
    SAMPLE_OUTPUT_1,
    SAMPLE_OUTPUT_2,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (SAMPLE_INPUT_1, SAMPLE_OUTPUT_1),
        (SAMPLE_INPUT_2, SAMPLE_OUTPUT_2),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"

import pytest

from aoc_2023.day_10.b import get_solution, solve
from aoc_2023.day_10.from_prompt import (
    PART_A_SOLUTION_1,
    PART_A_SOLUTION_2,
    PART_A_SOLUTION_3,
    PART_B_SAMPLE_1,
    PART_B_SAMPLE_2,
    PART_B_SAMPLE_3,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        (PART_B_SAMPLE_1, PART_A_SOLUTION_1),
        (PART_B_SAMPLE_2, PART_A_SOLUTION_2),
        (PART_B_SAMPLE_3, PART_A_SOLUTION_3),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


def test_my_solution():
    assert get_solution() == 529

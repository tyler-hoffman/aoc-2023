import pytest

from aoc_2023.day_16.b import get_solution, solve


@pytest.mark.parametrize(
    "input, expected",
    [
        ("INPUT", -1),
    ],
)
def test_solve(input: str, expected: int):
    assert solve(input) == expected


@pytest.mark.skip
def test_my_solution():
    assert get_solution() == "NOT THIS"

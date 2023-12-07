import pytest
from aoc_2023.day_07.a import get_solution, solve
from aoc_2023.day_07.common import Hand
from aoc_2023.day_07.from_prompt import SAMPLE_DATA, SAMPLE_SOLUTION


@pytest.mark.parametrize(
    "smaller, larger",
    [
        (Hand("2AAAA", 0), Hand("33332", 0)),
        (Hand("77788", 0), Hand("77888", 0)),
    ],
)
def test_compare(smaller: Hand, larger: Hand):
    assert smaller < larger


def test_solve():
    assert solve(SAMPLE_DATA) == SAMPLE_SOLUTION


def test_my_solution():
    assert get_solution() == 251121738

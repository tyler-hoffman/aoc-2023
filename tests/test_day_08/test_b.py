from aoc_2023.day_08.b import get_solution, solve
from aoc_2023.day_08.from_prompt import SAMPLE_DATA_B, SAMPLE_SOLUTION_B


def test_solve():
    assert solve(SAMPLE_DATA_B) == SAMPLE_SOLUTION_B


def test_my_solution():
    assert get_solution() < 106436333295260362798271
    assert get_solution() < 106436333295260362798271
    assert get_solution() == "NOT THIS"

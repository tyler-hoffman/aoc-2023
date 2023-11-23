def create_part_test_stub(day_string: str, part: str) -> str:
    src = "aoc_2023"
    return _TEST_PART_TEMPLATE.format(
        day_string=day_string,
        part=part,
        part_upper=part.upper(),
        src=src,
    )


_TEST_PART_TEMPLATE = """
import pytest

from {src}.day_{day_string}.{part} import get_solution, solve


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

"""

import pytest

from aoc_2023.tools.factors import get_prime_factors


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, {}),
        (2, {2: 1}),
        (3, {3: 1}),
        (6, {2: 1, 3: 1}),
        (18, {2: 1, 3: 2}),
    ],
)
def test_get_prime_factors(input: int, expected: int):
    assert get_prime_factors(input) == expected

import pytest

from aoc_2023.tools.factors import get_prime_factors, smallest_product_of_all_factors


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


@pytest.mark.parametrize(
    "input, expected",
    [
        ([2], 2),
        ([2, 4], 4),
        ([6, 9], 18),
    ],
)
def test_smallest_product_of_all_factors(input: list[int], expected: int):
    assert smallest_product_of_all_factors(input) == expected

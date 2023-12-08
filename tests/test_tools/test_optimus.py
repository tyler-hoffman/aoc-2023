import pytest

from aoc_2023.tools.optimus import Optimus


@pytest.mark.parametrize(
    "input, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
    ],
)
def test_is_prime(input: int, expected: bool):
    optimus = Optimus()
    assert optimus.is_prime(input) is expected


def test_get_primes():
    optimus = Optimus()
    primes = optimus.get_all()
    first_couple = [next(primes) for _ in range(5)]
    assert first_couple == [2, 3, 5, 7, 11]

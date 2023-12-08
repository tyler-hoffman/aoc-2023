from typing import Mapping

from aoc_2023.tools.optimus import Optimus


def get_prime_factors(x: int) -> Mapping[int, int]:
    """Get a mapping of prime factors to their counts."""
    remaining = x
    output = dict[int, int]()
    all_primes = Optimus().get_all()

    while remaining > 1:
        prime = next(all_primes)
        count = 0
        while remaining % prime == 0:
            count += 1
            remaining //= prime
        if count:
            output[prime] = count

    return output

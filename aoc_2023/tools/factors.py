from typing import Collection, Mapping

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


def smallest_product_of_all_factors(values: Collection[int]) -> int:
    """IDK the right name for this."""
    factor_sets = [get_prime_factors(v) for v in values]

    relevant_primes = set[int]()
    for factors in factor_sets:
        relevant_primes.update(set(factors.keys()))

    output_factors = dict[int, int]()
    for prime in relevant_primes:
        for factor in factor_sets:
            output_factors[prime] = max(
                factor.get(prime, 0), output_factors.get(prime, 0)
            )

    output = 1
    for k, v in output_factors.items():
        output *= k**v
    return output

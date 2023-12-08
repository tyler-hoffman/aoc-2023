from typing import Iterator


class Optimus:
    _highest_checked: int = 2
    _known_non_primes: set[int] = {1}
    _known_primes: set[int] = {2}
    _highest_prime: int = 2

    def is_prime(self, x: int) -> bool:
        assert x > 0, "Come on man, it's gotta be positive"

        highest = self._highest_checked
        if x > highest:
            for p in self._known_primes:
                m = highest - highest % p
                while m <= x:
                    self._known_non_primes.add(m)
                    m += p
            for n in range(highest, x + 1):
                if n not in self._known_non_primes:
                    self._highest_prime = n
                    self._known_primes.add(n)
            self._highest_checked = x
        return x in self._known_primes

    def get_all(self) -> Iterator[int]:
        i = 1
        while True:
            if self.is_prime(i):
                yield i
            i += 1

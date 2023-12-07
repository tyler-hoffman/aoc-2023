from collections import defaultdict
from typing import Collection, TypeVar


T = TypeVar("T")


def frequency_map(data: Collection[T]) -> defaultdict[T, int]:
    output = defaultdict[T, int](int)

    for datum in data:
        output[datum] += 1

    return output

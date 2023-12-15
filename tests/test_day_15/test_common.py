from aoc_2023.day_15.common import hash_it
from aoc_2023.day_15.from_prompt import HASH, HASH_HASHED


def test_hash():
    assert hash_it(HASH) == HASH_HASHED

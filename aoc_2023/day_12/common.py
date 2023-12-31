from dataclasses import dataclass
import re
from functools import cache


@dataclass(frozen=True)
class Record:
    chars: str
    congruencies: list[int]


PERIOD_PATTERN = re.compile(r"\.+")


@cache
def solve_it(
    chars: str,
    congruencies: tuple[int, ...],
) -> int:
    if len(congruencies) == 0:
        output = 1 if all(ch != "#" for ch in chars) else 0
        return output
    elif len(congruencies) == 1:
        return congruency_matches(chars, congruencies[0])
    else:
        if len(chars) == 0:
            return 0
        mid = len(chars) // 2
        mid_char = chars[mid]
        if mid_char == ".":
            return split_as_period(chars, congruencies)
        elif mid_char == "#":
            return split_as_hash(chars, congruencies)
        elif mid_char == "?":
            return sum(
                [
                    split_as_period(chars, congruencies),
                    split_as_hash(chars, congruencies),
                ]
            )
        else:
            assert False


@cache
def congruency_matches(chars: str, congruency: int) -> int:
    full_string = "".join(chars)
    if congruency == 0:
        return 1 if "#" not in chars else 0
    groups = [g for g in PERIOD_PATTERN.split(full_string) if g]
    with_hashes = [g for g in groups if "#" in g]
    match len(with_hashes):
        case 0:
            output = 0
            for group in groups:
                if len(group) >= congruency:
                    output += len(group) + 1 - congruency
            return output
        case 1:
            string = with_hashes[0]
            hash_start = string.index("#")
            hash_end = len(string) - string[::-1].index("#")
            length = hash_end - hash_start
            if length > congruency:
                return 0
            else:
                output = 0
                for start in range(1 + len(string) - congruency):
                    end = start + congruency
                    if start > hash_start:
                        ...
                    elif end < hash_end:
                        ...
                    else:
                        output += 1
                return output

        case _:
            return 0


def split_as_period(chars: str, congruencies: tuple[int, ...]) -> int:
    mid = len(chars) // 2
    assert chars[mid] != "#"
    left_chars = chars[:mid]
    right_chars = chars[mid + 1 :]
    output = 0
    for i in range(len(congruencies) + 1):
        left = solve_it(left_chars, congruencies[:i])
        right = solve_it(right_chars, congruencies[i:])
        output += left * right
    return output


def split_as_hash(chars: str, congruencies: tuple[int, ...]) -> int:
    output = 0
    mid = len(chars) // 2
    assert chars[mid] != "."
    congruency_count = len(congruencies)
    output = 0
    for c in range(congruency_count):
        congruency = congruencies[c]
        for to_the_left in range(congruency):
            left = mid - to_the_left
            right = left + congruency
            if left < 0:
                continue
            if right > len(chars):
                continue
            if "." in chars[left:right]:
                continue
            if left > 0 and chars[left - 1] == "#":
                continue
            if right < len(chars) and chars[right] == "#":
                continue

            left_count = solve_it(chars[: max(0, left - 1)], congruencies[:c])
            right_count = solve_it(chars[right + 1 :], congruencies[c + 1 :])
            output += left_count * right_count
    return output

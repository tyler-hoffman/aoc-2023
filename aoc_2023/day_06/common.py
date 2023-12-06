from dataclasses import dataclass


@dataclass(frozen=True)
class Race:
    time: int
    distance: int


def solutions_for_race(race: Race) -> int:
    assert can_win(race, race.time // 2)
    bottom = get_bottom_hold_time(race)
    top = get_top_hold_time(race)

    output = top - bottom + 1
    return output


def get_top_hold_time(race: Race) -> int:
    return first_instance(race, go_up=True) - 1


def get_bottom_hold_time(race: Race) -> int:
    return first_instance(race, go_up=False)


def first_instance(race: Race, go_up: bool) -> int:
    left = 0
    right = race.time
    while left < right:
        mid = (left + right) // 2
        if can_win(race, mid) == go_up:
            left = mid + 1
        else:
            right = mid
    return left


def can_win(race: Race, hold_time: int) -> bool:
    speed = hold_time
    boat_time = race.time - hold_time
    dist = speed * boat_time
    return dist > race.distance

from aoc_2023.day_06.common import Race


class Parser:
    @staticmethod
    def parse(input: str) -> list[Race]:
        time_line, dist_line = input.strip().splitlines()
        times = [int(x) for x in time_line.split()[1:]]
        dists = [int(x) for x in dist_line.split()[1:]]
        return [Race(time=t, distance=d) for t, d in zip(times, dists)]

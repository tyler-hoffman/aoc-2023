def create_part_stub(day_string: str, part: str) -> str:
    src = "aoc_2023"
    return _PART_TEMPLATE.format(
        day_string=day_string,
        part_upper=part.upper(),
        src=src,
    )


_PART_TEMPLATE = """
from dataclasses import dataclass
from {src}.day_{day_string}.parser import Parser


@dataclass
class Day{day_string}Part{part_upper}Solver:
    input: str

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day{day_string}Part{part_upper}Solver(data)

    return solver.solution

def get_solution() -> int:
    with open("aoc_2023/day_{day_string}/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

"""

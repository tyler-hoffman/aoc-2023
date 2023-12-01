from aoc_2023.day_01.parser import Parser
from aoc_2023.day_01.solver import Day01Solver


num_map = {str(x): x for x in range(10)}


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day01Solver(data, num_map)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_01/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

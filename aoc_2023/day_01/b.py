from aoc_2023.day_01.parser import Parser
from aoc_2023.day_01.solver import Day01Solver

number_strings = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

word_map = {word: i + 1 for i, word in enumerate(number_strings)}
digit_map = {str(x): x for x in range(10)}

num_map = word_map | digit_map


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

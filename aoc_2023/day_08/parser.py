from aoc_2023.day_08.common import Data, Node


class Parser:
    @staticmethod
    def parse(input: str) -> Data:
        lines = input.strip().splitlines()

        directions = Parser.parse_directions(lines[0])
        nodes = Parser.parse_nodes(lines[2:])

        return Data(directions, nodes)

    @staticmethod
    def parse_directions(line: str) -> list[str]:
        return [x for x in line]

    @staticmethod
    def parse_nodes(lines: list[str]) -> list[Node]:
        return [Parser.parse_node(line) for line in lines]

    @staticmethod
    def parse_node(line: str) -> Node:
        name, rest = line.split(" = ")
        in_parens = rest[1:-1]
        left, right = in_parens.split(", ")

        return Node(name, left, right)

from aoc_2023.day_19.common import (
    Data,
    GreaterThan,
    LessThan,
    Part,
    Predicate,
    Workflow,
    Yes,
)


class Parser:
    @staticmethod
    def parse(input: str) -> Data:
        first, second = input.strip().split("\n\n")

        workflows = [Parser.parse_workflow(line) for line in first.splitlines()]
        parts = [Parser.parse_part(line) for line in second.splitlines()]

        return Data(workflows=workflows, parts=parts)

    @staticmethod
    def parse_part(line: str) -> Part:
        x, m, a, s = [int(x[2:]) for x in line[1:-1].split(",")]

        return Part(x, m, a, s)

    @staticmethod
    def parse_workflow(line: str) -> Workflow:
        name, rules_str = line[:-1].split("{")
        rules = [Parser.parse_rule(rule) for rule in rules_str.split(",")]

        return Workflow(name, rules)

    @staticmethod
    def parse_rule(line: str) -> Predicate:
        if "<" in line:
            first, dest = line.split(":")
            field, target = first.split("<")
            return LessThan(dest=dest, field=field, target=int(target))
        elif ">" in line:
            first, dest = line.split(":")
            field, target = first.split(">")
            return GreaterThan(dest=dest, field=field, target=int(target))
        else:
            return Yes(dest=line)

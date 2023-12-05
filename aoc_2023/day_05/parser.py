from aoc_2023.day_05.common import Data, Mapping, MappingSet


class Parser:
    @staticmethod
    def parse(input: str) -> Data:
        groups = input.strip().split("\n\n")
        seeds = Parser.parse_seed_line(groups[0])
        mapping_sets = [Parser.parse_mapping_set(x) for x in groups[1:]]
        return Data(seeds=seeds, mapping_sets=mapping_sets)

    @staticmethod
    def parse_seed_line(line: str) -> list[int]:
        label, data = line.split(": ")
        strings = data.split()
        return [int(x) for x in strings]

    @staticmethod
    def parse_mapping_set(input: str) -> MappingSet:
        lines = input.splitlines()
        name = lines[0][:-1]
        mappings = [Parser.parse_mapping(x) for x in lines[1:]]
        return MappingSet(name=name, mappings=mappings)

    @staticmethod
    def parse_mapping(line: str) -> Mapping:
        destination, source, range = [int(x) for x in line.split()]
        return Mapping(destination=destination, source=source, range=range)

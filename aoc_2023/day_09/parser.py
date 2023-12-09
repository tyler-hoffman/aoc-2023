class Parser:
    @staticmethod
    def parse(input: str) -> list[list[int]]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> list[int]:
        return [int(x) for x in line.split()]

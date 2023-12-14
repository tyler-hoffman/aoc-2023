class Parser:
    @staticmethod
    def parse(input: str) -> list[list[list[str]]]:
        chunks = input.strip().split("\n\n")
        return [Parser.parse_land_map(chunk) for chunk in chunks]

    @staticmethod
    def parse_land_map(input: str) -> list[list[str]]:
        lines = input.strip().splitlines()

        return [list(line) for line in lines]

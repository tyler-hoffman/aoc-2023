class Parser:
    @staticmethod
    def parse(input: str) -> list[list[str]]:
        lines = input.strip().splitlines()
        return [list(line) for line in lines]

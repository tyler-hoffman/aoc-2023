class Parser:
    @staticmethod
    def parse(input: str) -> list[list[int]]:
        lines = input.strip().splitlines()
        return [[int(x) for x in line] for line in lines]

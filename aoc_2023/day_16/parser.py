class Parser:
    @staticmethod
    def parse(input: str) -> list[str]:
        lines = input.strip().splitlines()
        lens = {len(line) for line in lines}
        assert len(lens) == 1
        return lines

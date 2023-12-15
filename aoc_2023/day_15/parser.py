from aoc_2023.day_15.common import Equal, Minus


class Parser:
    @staticmethod
    def parse_lines(input: str) -> list[str]:
        return input.strip().split(",")

    @staticmethod
    def parse_operations(input: str) -> list[Equal | Minus]:
        lines = Parser.parse_lines(input)
        output = list[Minus | Equal]()
        for line in lines:
            if line[-1] == "-":
                output.append(Minus(line[:-1]))
            else:
                label, val = line.split("=")
                output.append(Equal(label, int(val)))
        return output

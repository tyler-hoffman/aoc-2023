import re
from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Value:
    value: str
    line_number: int
    start: int
    end: int


@dataclass(frozen=True)
class Bounds:
    x1: int
    x2: int
    y1: int
    y2: int


@dataclass
class Analyzer:
    lines: list[str]

    @cached_property
    def height(self) -> int:
        return len(self.lines)

    @cached_property
    def width(self) -> int:
        return len(self.lines[0])

    @cached_property
    def part_numbers(self) -> set[Value]:
        output = set[Value]()
        for value in self.numbers:
            box = self.bounding_box(value)
            bounds = [
                self.lines[y][box.x1 : box.x2]
                for y in range(box.y1, min(self.height, box.y2 + 1))
            ]
            chars = "".join(bounds)
            if self.symbol_regex.search(chars) is not None:
                output.add(value)
        return output

    def bounding_box(self, value: Value) -> Bounds:
        x1 = max(0, value.start - 1)
        x2 = min(self.width, value.end + 1)
        y1 = max(0, value.line_number - 1)
        y2 = min(self.height, value.line_number + 1)

        return Bounds(x1=x1, x2=x2, y1=y1, y2=y2)

    @cached_property
    def numbers(self) -> set[Value]:
        return self.get_values(self.number_regex)

    @cached_property
    def stars(self) -> set[Value]:
        return self.get_values(self.star_regex)

    def get_values(self, pattern: re.Pattern) -> set[Value]:
        output = set[Value]()

        for i, line in enumerate(self.lines):
            for m in pattern.finditer(line):
                output.add(
                    Value(
                        value=m.group(0),
                        start=m.start(),
                        end=m.end(),
                        line_number=i,
                    )
                )

        return output

    @cached_property
    def number_regex(self) -> re.Pattern:
        return re.compile(r"(\d+)")

    @cached_property
    def star_regex(self) -> re.Pattern:
        return re.compile(r"\*")

    @cached_property
    def symbol_regex(self) -> re.Pattern:
        return re.compile(r"[^0-9.]")

from dataclasses import dataclass, field
from functools import cached_property
from aoc_2023.day_15.common import Equal, Minus, hash_it
from aoc_2023.day_15.parser import Parser


@dataclass
class Lens:
    label: str
    focus_length: int
    deleted: bool = False


@dataclass(frozen=True)
class Box:
    id: int
    lenses: list[Lens] = field(hash=False, default_factory=list)
    lens_index_lookup: dict[str, Lens] = field(hash=False, default_factory=dict)

    @property
    def focusing_power(self) -> int:
        output = 0
        box_num = self.id + 1
        lenses = [lens for lens in self.lenses if not lens.deleted]
        for i, lens in enumerate(lenses):
            lens_num = i + 1
            output += box_num * lens_num * lens.focus_length

        return output

    def remove_lens(self, label: str) -> None:
        if label in self.lens_index_lookup:
            self.lens_index_lookup[label].deleted = True
            del self.lens_index_lookup[label]

    def set_lens(self, label: str, value) -> None:
        if label in self.lens_index_lookup:
            lens = self.lens_index_lookup[label]
            lens.focus_length = value
        else:
            lens = Lens(label, value)
            self.lenses.append(lens)
            self.lens_index_lookup[label] = lens


@dataclass
class Day15PartBSolver:
    operations: list[Equal | Minus]

    @property
    def solution(self) -> int:
        for op in self.operations:
            self.do_operation(op)
        return sum(box.focusing_power for box in self.boxes)

    @cached_property
    def boxes(self) -> list[Box]:
        return [Box(i, []) for i in range(256)]

    def do_operation(self, op: Minus | Equal) -> None:
        box_id = hash_it(op.label)
        box = self.boxes[box_id]

        match op:
            case Minus(label):
                box.remove_lens(label)
            case Equal(label, val):
                box.set_lens(label, val)


def solve(input: str) -> int:
    operations = Parser.parse_operations(input)
    solver = Day15PartBSolver(operations)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2023/day_15/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())

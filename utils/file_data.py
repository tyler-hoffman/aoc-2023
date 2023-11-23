import dataclasses
from typing import Literal, Union

Part = Union[Literal["a"], Literal["b"]]


@dataclasses.dataclass
class FileData(object):
    """Dataclass to handle any directory/file names
    to be used when bootstrapping files
    """

    src = "aoc_2023"
    tests = "tests"

    day: int
    part: Part

    @property
    def day_string(self) -> str:
        return f"{self.day:02d}"

    @property
    def part_module(self) -> str:
        return f"{self.src}.day_{self.day_string}.{self.part}"

    @property
    def directory(self) -> str:
        return f"{self.src}/day_{self.day_string}"

    @property
    def test_directory(self) -> str:
        return f"{self.tests}/test_day_{self.day_string}"

    @property
    def input_file(self) -> str:
        return f"{self.directory}/input.txt"

    @property
    def part_file(self) -> str:
        return f"{self.directory}/{self.part}.py"

    @property
    def parser_file(self) -> str:
        return f"{self.directory}/parser.py"

    @property
    def prompt_file(self) -> str:
        return f"{self.directory}/from_prompt.py"

    @property
    def solver_file(self) -> str:
        return f"{self.directory}/solver.py"

    @property
    def test_part_file(self) -> str:
        return f"{self.test_directory}/test_{self.part}.py"

    @property
    def test_data_file(self) -> str:
        return f"{self.test_directory}/sample_data.py"

    @property
    def src_init_file(self) -> str:
        return self._init_file(self.directory)

    @property
    def test_init_file(self) -> str:
        return self._init_file(self.test_directory)

    def _init_file(self, directory: str) -> str:
        return f"{directory}/__init__.py"

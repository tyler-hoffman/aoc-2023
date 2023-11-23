import argparse
import os

import aocd

from utils.file_data import FileData
from utils.templates.parser import create_parser_stub
from utils.templates.part import create_part_stub
from utils.templates.test_part import create_part_test_stub


def touch_file(path: str) -> None:
    open(path, "x")


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content.strip() + "\n")


def create_directories_if_needed(file_data: FileData) -> None:
    if not os.path.isdir(file_data.directory):
        os.makedirs(file_data.directory)
        touch_file(file_data.src_init_file)
        write_file(file_data.input_file, aocd.get_data(year=2023, day=file_data.day))
        write_file(file_data.parser_file, create_parser_stub())
        write_file(file_data.prompt_file, "")

    if not os.path.isdir(file_data.test_directory):
        os.makedirs(file_data.test_directory)
        touch_file(file_data.test_init_file)


def create_part_files(file_data: FileData) -> None:
    write_file(
        file_data.part_file,
        create_part_stub(day_string=file_data.day_string, part=file_data.part),
    )

    write_file(
        file_data.test_part_file,
        create_part_test_stub(day_string=file_data.day_string, part=file_data.part),
    )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("-d", "--day", type=int, help="Day to create files for")
    parser.add_argument(
        "-p",
        "--part",
        choices=["a", "b"],
        help="Part to create files for",
    )

    return parser


if __name__ == "__main__":
    args = create_parser().parse_args()

    file_data = FileData(day=args.day, part=args.part)

    create_directories_if_needed(file_data)
    create_part_files(file_data)

from typing import Any

import requests
import datetime
import dotenv
from pathlib import Path


def read_puzzle_input(input_path: str) -> list[str]:
    with open(input_path, "r") as f:
        return f.read().splitlines()


def get_puzzle_input(y: int = None, d: int = None) -> list[str]:
    """Fetches Advent of Code puzzle input

    It reads a session cookie variable from a .env file in the parent directory.

    Args:
        y: Don't set to get today's puzzle input. Set to get any day.
        d: Don't set to get today's puzzle input. Set to get any year.

    Returns:
        object: Puzzle input
    """

    # Possibility to fetch any puzzle input or today's input
    today = datetime.date.today()
    if d is None and y is None:
        if int(today.month) != 12:
            raise Exception(f"There is no Advent of Code puzzle for {today}!")
        day = int(today.day)
        year = int(today.year)
    else:
        day = d
        year = y

    puzzle_input_file = f"aoc_{year}_{day:02d}_input.txt"

    # Let's go easy on the webserver hosting the Advent of Code event and
    # download the puzzle input to a local file in case it doesn't exist yet
    if not Path(puzzle_input_file).exists():
        dotenv.load_dotenv()
        COOKIE = dotenv.get_key("../.env", "AOC_SESSION_COOKIE")

        session = requests.Session()
        download_todays_input = session.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": COOKIE},
        )
        todays_input_text = download_todays_input.text

        with open(puzzle_input_file, "w") as f:
            f.write(todays_input_text)

    # In case the file exists, just read it locally.
    # No point downloading it again.
    return read_puzzle_input(input_path=puzzle_input_file)


def choose_puzzle_input(
    y: int = None, d: int = None, sample_input_path: str = None
):
    if not sample_input_path:
        return get_puzzle_input(y=y, d=d)
    else:
        return read_puzzle_input(input_path=sample_input_path)


def make_chunks(chunk_size: int, iterable: list) -> list:
    chunks = []
    for i in range(0, len(iterable), chunk_size):
        chunks.append(iterable[i : i + chunk_size])
    return chunks


def print_solution(solution: Any, y: int, d: int, part: int) -> None:
    print(f"{d:02d}.12.{y} {part}: {solution}")

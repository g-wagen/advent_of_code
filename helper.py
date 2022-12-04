from typing import Any

import requests
import datetime
import os
import dotenv


def get_puzzle_input(y=None, d=None):
    """Fetches Advent of Code puzzle input

    It reads a session cookie variable from a .env file in the parent directory.

    :param d: Don't set to get today's puzzle input. Set to get any day.
    :type d: int
    :param y: Don't set to get today's puzzle input. Set to get any year.
    :type y: int
    """

    puzzle_input = None

    # Possibility to fetch any puzzle input or today's input
    today = datetime.datetime.now()
    if d is None and y is None:
        day = int(today.strftime('%d'))
        year = int(today.strftime('%Y'))
    else:
        day = d
        year = y

    puzzle_input_file = f'aoc_{year}_{day:02d}_input.txt'

    # Let's go easy on the webserver hosting the Advent of Code event and
    # download the puzzle input to a local file in case it doesn't exist yet
    if not os.path.exists(puzzle_input_file):
        dotenv.load_dotenv()
        COOKIE = dotenv.get_key('../.env', 'AOC_SESSION_COOKIE')

        session = requests.Session()
        download_todays_input = session.get(
            f'https://adventofcode.com/{year}/day/{day}/input',
            cookies={'session': COOKIE})
        todays_input_text = download_todays_input.text

        with open(puzzle_input_file, 'w') as f:
            f.write(todays_input_text)

    # In case the file exists, just read it locally.
    # No point downloading it again.
    with open(puzzle_input_file, 'r') as f:
        puzzle_input = f.read().splitlines()

    return puzzle_input


def make_chunks(chunk_size, iterable):
    chunks = []
    for i in range(0, len(iterable), chunk_size):
        chunks.append(iterable[i:i+chunk_size])
    return chunks


def print_solution(solution: Any, y: int, d: int, part: int):
    print(f'{d:02d}.12.{y} {part}: {solution}')

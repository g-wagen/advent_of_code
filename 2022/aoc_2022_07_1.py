from helper import get_puzzle_input
from pathlib import Path
import shutil
import os

puzzle_input = get_puzzle_input(y=2022, d=7)

# with open('aoc_2022_07_input_sample.txt', 'r') as f:
#     puzzle_input = f.read().splitlines()

# delete file structure if it exists
root_dir = (Path(__file__).parents[0] / 'aoc_2022_07')
if Path(root_dir).exists():
    shutil.rmtree(root_dir)


# build the damn directory tree
for line in puzzle_input:
    parts = line.split()
    if '/' in line:
        try:
            os.mkdir(root_dir)
        except FileExistsError:
            pass
        os.curdir = root_dir
    elif 'dir' == parts[0]:
        try:
            os.mkdir(str(Path(os.curdir) / parts[1]))
        except FileExistsError:
            ...
    elif parts[0].isdigit():
        with open(os.path.join(os.curdir, parts[1]), 'a') as f:
            write_this = ''.join([str(1) for x in range(int(parts[0]))])
            f.write(write_this)
    elif parts[1] == 'cd':
        if parts[2] == '..':
            os.curdir = str(Path(os.curdir).parent)
        else:
            os.curdir = str(Path(os.curdir) / parts[2])


def get_file_size(the_file: str) -> int:
    if Path(the_file).is_file():
        return Path(the_file).stat().st_size
    else:
        return 0


directories = {}
filepath = str(Path(Path(__file__).parents[0] / 'aoc_2022_07'))


def get_all_dirs(start):
    directories = []
    for root, dirs, files in os.walk(start):
        for d in dirs:
            directories.append(str(Path(root, d)))
    return directories


def recursive_file_sizes(start):
    sizes = 0
    for root, dirs, files in os.walk(start):
        for f in files:
            sizes += get_file_size(str(Path(root, f)))
    return sizes


def this_folder_size(folderpath):
    return sum([get_file_size(x) for x in os.listdir(folderpath) if Path(x).is_file()])


dirs_and_sizes = dict()

# for dir in get_all_dirs(filepath):
#     whole_folder_size = recursive_file_sizes(dir)
#     if whole_folder_size <= 100000:
#         dirs_and_sizes[whole_folder_size] = dir

for dir in get_all_dirs(filepath):
    folder_contents = os.listdir(dir)
    folder_size = sum([get_file_size(str(Path(dir, x))) for x in folder_contents])
    if folder_size <= 100000:
        dirs_and_sizes[folder_size] = dir

total = 0

for k, v in sorted(dirs_and_sizes.items(), key=lambda x: x[1]):
    print(v.replace(filepath, '').split('/')[1:])
    # print(f'{k:05d}', v)
    total += k

print(total)

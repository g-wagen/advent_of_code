from helper import choose_puzzle_input, print_solution

year = 2023
day = 15

puzzle_input = choose_puzzle_input(
    y=year,
    d=day,
    # sample_input_path=f"aoc_{year}_{day:02d}_input_sample.txt",
)


def hash_alg(sequence: str) -> int:
    out = 0
    for item in sequence:
        out += ord(item)
        out *= 17
        out = out % 256
    return out


def lens_and_box_id(sequence: str) -> str:
    return sequence[:-1] if "-" in sequence else sequence[:-2]


def focal_length(sequence: str) -> int:
    return int(sequence.split("=")[-1]) if "=" in sequence else -1


boxes = {}

for wtf in puzzle_input[0].split(","):
    box = lens_and_box_id(wtf)
    boxes[hash_alg(box)] = {}


for wtf in puzzle_input[0].split(","):
    f = focal_length(wtf)
    lens_id = lens_and_box_id(wtf)
    box_number = hash_alg(lens_id)

    if f > -1:
        boxes[box_number].update({lens_id: f})
    else:
        if boxes[box_number].get(lens_id):
            boxes[box_number].pop(lens_id)

focus_power = []

for box, lenses in boxes.items():
    for pos, (lens, focal) in enumerate(lenses.items()):
        focus_power.append((box + 1) * focal * (pos + 1))

print_solution(solution=sum(focus_power), y=year, d=day, part=2)

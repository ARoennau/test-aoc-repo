import sys
from typing import Set, Tuple
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print("No file provided")
    exit()

input = list(readfile_string(f"{sys.argv[1]}.txt"))[0]


def parse_input(input: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    _, _, x_section, y_section = input.split(" ")
    x_section = x_section[2:-1]
    y_section = y_section[2:]
    x_min, x_max = map(lambda str: int(str), x_section.split(".."))
    y_min, y_max = map(lambda str: int(str), y_section.split(".."))
    return (x_min, x_max), (y_min, y_max)


def calculate_trajectory(input: str):
    x_range, y_range = parse_input(input)
    valid_xs = get_valid_xs(x_range)
    steps = get_steps(valid_xs)
    result = find_highest_y_start(steps, y_range)
    return result


def get_steps(valid_xs: Set[Tuple[int, int]]) -> Set[int]:
    result = set()
    for _, steps in valid_xs:
        result.add(steps)
    return result


def get_valid_xs(x_range: Tuple[int, int]) -> Set[Tuple[int, int]]:
    min, max = x_range
    valid_xs: Set[Tuple[int, int]] = set()
    for i in range(1, max):
        velocity = i - 1
        current = i
        steps = 1
        while current < max:
            if current >= min:
                valid_xs.add((i, steps))
            if velocity <= 0:
                break
            steps += 1
            current += velocity
            velocity -= 1
    return valid_xs


def find_highest_y_start(steps: Set[int], y_range: Tuple[int, int]):
    highest_y = (y_range[1], y_range[1])
    for step_count in steps:
        y = highest_y[0]
        while y < 200:
            current_highest = get_highest_y(step_count, y, y_range)
            if current_highest > highest_y[1]:
                highest_y = (y, current_highest)
            y += 1

    return highest_y


def get_highest_y(steps: int, y_start: int, y_range: Tuple[int, int]) -> int:
    total = y_start
    velocity = y_start - 1
    highest_y = y_start
    for _ in range(1, steps):
        total += velocity
        highest_y = max(highest_y, total)
        velocity -= 1

    if total < y_range[0]:
        return y_range[0]

    while total >= y_range[0]:
        highest_y = max(highest_y, total)
        if total <= y_range[1]:
            return highest_y
        total += velocity
        velocity -= 1
    return y_range[0]


print(calculate_trajectory(input))

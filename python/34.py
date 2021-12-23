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
    starts = calculate_all_starts(x_range, y_range)
    return len(starts)


def calculate_all_starts(
    x_range: Tuple[int, int], y_range: Tuple[int, int]
) -> Set[Tuple[int, int]]:
    starts: Set[Tuple[int, int]] = set()
    for start_x in range(5, x_range[1] + 1):
        for start_y in range(y_range[0], 200):
            # for start_y in range(y_range[0], 10):
            current_x = 0
            current_y = 0
            velocity_x = start_x
            velocity_y = start_y
            found = False
            while is_iterating(current_x, current_y, velocity_x, x_range, y_range):
                if is_in_target(current_x, current_y, x_range, y_range):
                    starts.add((start_x, start_y))
                    found = True
                    break
                current_x += velocity_x
                current_y += velocity_y
                velocity_x -= 1
                velocity_y -= 1

            if found:
                continue

            if current_x >= x_range[0] and current_x <= x_range[1]:
                # print(start_y)
                if y_in_target(current_y, velocity_y, y_range):
                    starts.add((start_x, start_y))
                continue
    return starts


def y_in_target(y: int, velocity: int, range: Tuple[int, int]):
    while y >= range[0]:
        if y <= range[1]:
            return True
        y += velocity
        velocity -= 1
    return False


def is_in_target(x: int, y: int, x_range: Tuple[int, int], y_range: Tuple[int, int]):
    return x >= x_range[0] and x <= x_range[1] and y >= y_range[0] and y <= y_range[1]


def is_iterating(
    x: int, y: int, x_velocity: int, x_range: Tuple[int, int], y_range: Tuple[int, int]
):
    return x <= x_range[1] and y >= y_range[0] and x_velocity > 0


print(calculate_trajectory(input))

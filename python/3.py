import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = readfile_string(f'{sys.argv[1]}.txt')


def calculate_distance(input):
    horizontal_total = 0
    depth_total = 0
    for command in input:
        split_command = command.split(' ')
        if split_command[0] == 'forward':
            horizontal_total += int(split_command[1])
        elif split_command[0] == 'down':
            depth_total += int(split_command[1])
        elif split_command[0] == 'up':
            depth_total -= int(split_command[1])

    return horizontal_total * depth_total


print(calculate_distance(input))

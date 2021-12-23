import sys
from utils.readfile import readfile_ints

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = readfile_ints(f'{sys.argv[1]}.txt')


def calculate_greater_sums(input):
    i = 1
    total = 0
    prev = input[0] + input[1] + input[2]
    while i < len(input) - 2:
        sum = input[i] + input[i + 1] + input[i + 2]
        if sum > prev:
            total += 1
        i += 1
        prev = sum
    return total


print(calculate_greater_sums(input))

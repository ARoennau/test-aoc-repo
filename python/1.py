import sys
from utils.readfile import readfile_ints


input = readfile_ints(f'{sys.argv[1]}.txt')


def calculate_total(input):
    i = 1
    total = 0
    while i < len(input):
        if input[i] > input[i - 1]:
            total += 1
        i += 1
    return total


print(calculate_total(input))

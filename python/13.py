import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(map(lambda str: int(str), list(
    readfile_string(f'{sys.argv[1]}.txt'))[0].split(',')))


def move_crabs(input):
    input.sort()
    mid = len(input) // 2
    median = input[mid]
    cost = sum_distances_fuel(input, median)
    return min(cost, min_left(input, median, cost), min_right(input, median, cost))


def min_left(input, median, median_cost):
    i = median - 1
    min = median_cost
    while i > input[0]:
        current_cost = sum_distances_fuel(input, i)
        if current_cost < min:
            min = current_cost
        else:
            return min

        i -= 1
    return min


def min_right(input, median, median_cost):
    i = median + 1
    min = median_cost
    while i < input[-1]:
        current_cost = sum_distances_fuel(input, i)
        if current_cost < min:
            min = current_cost
        else:
            return min

        i += 1
    return min


def sum_distances_fuel(input, point):
    total = 0
    for number in input:
        distance = abs(number - point)
        total += (distance * (distance + 1)) // 2

    return total


print(move_crabs(input))

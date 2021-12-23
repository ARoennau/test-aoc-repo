import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def generate_array(input):
    array = []
    for line in input:
        new_line = list(map(lambda str: int(str), [c for c in line]))
        array.append(new_line)
    return array


def count_flahses(input):
    array = generate_array(input)
    total = 0
    for i in range(0, 100):
        total += run_step(array)
        # print('step', i,  array)
    return total


def run_step(array):
    total = 0
    for i, row in enumerate(array):
        for j, number in enumerate(row):
            if number == -1:
                continue
            array[i][j] += 1
            if array[i][j] > 9:
                total += increment_neighbors(array, i, j)

    for i, row in enumerate(array):
        for j, number in enumerate(row):
            if number == -1:
                array[i][j] = 0
    return total


def increment_neighbors(array, row, col):
    array[row][col] = -1
    total = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row = row + i
            new_col = col + j
            if new_row >= len(array) or new_row < 0 or new_col >= len(array[0]) or new_col < 0 or array[new_row][new_col] == -1:
                continue
            array[new_row][new_col] += 1
            if array[new_row][new_col] > 9:
                total += increment_neighbors(array, new_row, new_col)
    return total


def clean_print_array(array):
    for line in array:
        print(line)


print(count_flahses(input))

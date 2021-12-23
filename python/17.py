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


def get_risk_total(input):
    array = generate_array(input)
    low_points = find_low_points(array)
    return sum_low_points(low_points)


def sum_low_points(low_points):
    total = len(low_points)
    for point in low_points:
        total += point
    return total


def find_low_points(input):
    low_points = []
    for i, row in enumerate(input):
        for j, number in enumerate(row):
            if is_low_point(input, i, j):
                low_points.append(number)
    return low_points


def is_low_point(input, row, col):
    number = input[row][col]
    for i in [-1, 1]:
        new_col = col + i
        new_row = row + i
        new_col_in_bounds = new_col >= 0 and new_col < len(input[0])
        new_row_in_bounds = new_row >= 0 and new_row < len(input)
        if (new_col_in_bounds and input[row][new_col] <= number) or (new_row_in_bounds and input[new_row][col] <= number):
            return False
    return True


print(get_risk_total(input))

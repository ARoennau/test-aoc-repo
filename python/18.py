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
    basins = find_basins(array, low_points)
    return calculate_result(basins)


def calculate_result(basins):
    b1, b2, b3 = find_three_largest_basins(basins)
    return b1 * b2 * b3


def find_three_largest_basins(basins):
    top_three = []
    for _ in range(0, 3):
        max_basin = -1
        for number in basins:
            max_basin = max(number, max_basin)
        top_three.append(max_basin)
        basins.remove(max_basin)
    return top_three


def find_basins(array, low_points):
    basins = []
    for low_point in low_points:
        basins.append(find_basin(array, low_point))
    return basins


def find_basin(array, low_point):
    queue = [low_point]
    basin_size = 0

    while len(queue) > 0:
        row, col = queue.pop(0)
        if array[row][col] == -1:
            continue
        array[row][col] = -1
        basin_size += 1

        for i in [-1, 1]:
            new_row = row + i
            new_col = col + i
            new_col_in_bounds = new_col >= 0 and new_col < len(array[0])
            new_row_in_bounds = new_row >= 0 and new_row < len(array)

            if new_col_in_bounds and array[row][new_col] not in [-1, 9]:
                queue.append((row, new_col))

            if new_row_in_bounds and array[new_row][col] not in [-1, 9]:
                queue.append((new_row, col))

    return basin_size


def find_low_points(input):
    low_points = []
    for i, row in enumerate(input):
        for j, _ in enumerate(row):
            if is_low_point(input, i, j):
                low_points.append((i, j))
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


def clean_print_array(array):
    for line in array:
        print(line)


print(get_risk_total(input))

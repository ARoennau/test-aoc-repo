import sys
from utils.readfile import readfile_line_segments

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = readfile_line_segments(f'{sys.argv[1]}.txt')


def find_dimensions(input):
    width = 0
    height = 0
    for row in input:
        for point in row:
            width = max(width, point[0])
            height = max(width, point[1])
    return width + 1, height + 1


def initializeMemo(width, height):
    memo = []
    for _ in range(0, height):
        row = []
        for _ in range(0, width):
            row.append(0)
        memo.append(row)
    return memo


def find_overlaps(input):
    width, height = find_dimensions(input)
    memo = initializeMemo(width, height)
    for row in input:
        plot_line(row, memo)
    return count_overlaps(memo)


def plot_line(row, memo):
    start = row[0]
    end = row[1]
    if start[0] == end[0]:
        plot_vertical_line(min(start[1], end[1]), max(
            start[1], end[1]), start[0], memo)
    elif start[1] == end[1]:
        plot_horizontal_line(min(start[0], end[0]), max(
            start[0], end[0]), start[1], memo)
    else:
        plot_diagonal_line(start, end, memo)


def plot_vertical_line(start, end, col, memo):
    for i in range(start, end + 1):
        memo[i][col] += 1


def plot_horizontal_line(start, end, row, memo):
    for i in range(start, end + 1):
        memo[row][i] += 1


def plot_diagonal_line(start, end, memo):
    xDirection = -1 if start[0] > end[0] else 1
    yDirection = -1 if start[1] > end[1] else 1

    currentX = start[0]
    currentY = start[1]
    while currentX != end[0] and currentY != end[1]:
        memo[currentY][currentX] += 1
        currentX += xDirection
        currentY += yDirection

    memo[currentY][currentX] += 1


def count_overlaps(memo):
    total = 0
    for row in memo:
        for number in row:
            total += 1 if number > 1 else 0
    return total


print(find_overlaps(input))

import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(map(lambda str: int(str), list(
    readfile_string(f'{sys.argv[1]}.txt'))[0].split(',')))


def count_fish(input):
    memo = initialize_memo(input)
    for _ in range(0, 256):
        simulate_day(memo)

    return sum_memo(memo)


def initialize_memo(input):
    memo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in input:
        memo[number] += 1
    return memo


def simulate_day(memo):
    for i in range(0, len(memo) - 1):
        swap(memo, i, i + 1)
    memo[-3] += memo[-1]


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def sum_memo(memo):
    total = 0
    for number in memo:
        total += number
    return total


print(count_fish(input))

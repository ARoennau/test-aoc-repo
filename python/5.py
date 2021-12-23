import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = readfile_string(f'{sys.argv[1]}.txt')


def power_consumption(input):
    totals = get_totals(input)
    gamma, epsion = generate_values(totals, len(input))
    return gamma * epsion


def get_totals(input):
    totals = []

    for bit in input[0]:
        totals.append(int(bit))

    for row in input[1:]:
        for i, bit in enumerate(row):
            totals[i] += int(bit)

    return totals


def generate_values(totals, n):
    half = n / 2
    gamma = 0
    epsilon = 0
    bit_value = pow(2, len(totals) - 1)
    for count in totals:
        if (count > half):
            gamma += bit_value
        else:
            epsilon += bit_value
        bit_value = int(bit_value / 2)

    return gamma, epsilon


print(power_consumption(input))

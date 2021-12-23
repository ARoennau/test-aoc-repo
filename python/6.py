import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = readfile_string(f'{sys.argv[1]}.txt')


def calculate_life_support(input):
    oxygen_generator = calculate_oxygen_generator(input)
    co2_scrubber = calculate_co2_scrubber(input)
    return convert_binary_to_int(oxygen_generator) * convert_binary_to_int(co2_scrubber)


def get_totals(input):
    totals = []

    for bit in input[0]:
        totals.append(int(bit))

    for row in input[1:]:
        for i, bit in enumerate(row):
            totals[i] += int(bit)

    return totals


def calculate_oxygen_generator(input):
    current_list = input
    for i in range(0, len(input[0])):
        if len(current_list) == 1:
            break

        total = get_total(current_list, i)
        goal = 1 if total >= len(current_list) / 2 else 0
        current_list = list(filter(lambda n: int(n[i]) == goal, current_list))

    return current_list[0]


def get_total(input, i):
    total = 0
    for number in input:
        total += int(number[i])
    return total


def calculate_co2_scrubber(input):
    current_list = input
    for i in range(0, len(input[0])):
        if len(current_list) == 1:
            break

        total = get_total(current_list, i)
        goal = 1 if total < len(current_list) / 2 else 0
        current_list = list(filter(lambda n: int(n[i]) == goal, current_list))

    return current_list[0]


def convert_binary_to_int(binary):
    bit_value = pow(2, len(binary) - 1)
    total = 0
    for number in binary:
        if (number == '1'):
            total += bit_value
        bit_value = int(bit_value / 2)
    return total


print(calculate_life_support(input))

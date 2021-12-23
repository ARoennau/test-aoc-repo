import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def split_lines(input):
    split_lines = []
    for row in input:
        split_lines.append(row.split(' | '))

    return sort_words(split_lines)


def sort_words(split_lines):
    lines = []
    for line in split_lines:
        new_line = []
        for portion in line:
            words = list(map(lambda word: ''.join(sorted(
                word)), portion.split(' ')))
            new_line.append(words)
        lines.append(new_line)
    return lines


def find_digits(input):
    lines = split_lines(input)
    total = 0
    for line in lines:
        digit_map = get_digit_map(line[0])
        total += get_number(line[1], digit_map)
    return total


def get_number(digits, digit_map):
    tens = 1000
    total = 0
    for digit in digits:
        total += digit_map.index(digit) * tens
        tens //= 10
    return total


def get_digit_map(digits):
    digit_map = ['', '', '', '', '', '', '', '', 'abcdefg', '']
    digit_map[1] = find_all_by_length(digits, 2)[0]
    digit_map[7] = find_all_by_length(digits, 3)[0]
    digit_map[4] = find_all_by_length(digits, 4)[0]
    length_five = find_all_by_length(digits, 5)
    digit_map[3] = find_by_substring(length_five, digit_map[7])
    length_five.remove(digit_map[3])
    determine_two_and_five(length_five, digit_map)
    length_six = find_all_by_length(digits, 6)
    digit_map[9] = find_by_substring(length_six, digit_map[4])
    length_six.remove(digit_map[9])
    digit_map[6] = find_by_substring(length_six, digit_map[5])
    length_six.remove(digit_map[6])
    digit_map[0] = length_six[0]
    return digit_map


def determine_two_and_five(digits, digit_map):
    four = digit_map[4]
    one = digit_map[1]
    difference = ''.join(c for c in four if c not in one)
    digit_map[5] = find_by_substring(digits, difference)
    digits.remove(digit_map[5])
    digit_map[2] = digits[0]


def find_by_substring(digits, letters):
    for digit in digits:
        if digit_includes(digit, letters):
            return digit
    return digits[-1]


def digit_includes(digit, letters):
    for letter in letters:
        if letter not in digit:
            return False
    return True


def find_all_by_length(digits: list[str], length: int):
    return list(filter(lambda digit: len(digit) == length, digits))


# find_digits(input)
print(find_digits(input))

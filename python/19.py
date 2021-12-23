import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def find_error_total(input):
    total = 0
    for line in input:
        total += error_score(line)
    return total


def error_score(line):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for character in line:
        if character in pairs.keys():
            stack.append(character)
        else:
            opener = stack.pop()
            if pairs[opener] != character:
                return score_map[character]
    return 0


print(find_error_total(input))

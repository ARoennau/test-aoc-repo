import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def find_error_total(input):
    scores = []
    for line in input:
        score = autocomplete_score(line)
        if score > 0:
            scores.append(score)
    return find_middle_score(scores)


def find_middle_score(scores):
    scores.sort()
    return scores[len(scores) // 2]


def autocomplete_score(line):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for character in line:
        if character in pairs.keys():
            stack.append(character)
        else:
            opener = stack.pop()
            if pairs[opener] != character:
                return 0

    return score_autocomplete(stack)


def score_autocomplete(stack):
    score_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    total = 0
    while len(stack) > 0:
        total *= 5
        total += score_map[stack.pop()]
    return total


print(find_error_total(input))

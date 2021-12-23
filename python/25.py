import sys
from utils.readfile import readfile_string

if len(sys.argv) < 2:
    print('No file provided')
    exit()

input = list(readfile_string(f'{sys.argv[1]}.txt'))


def split_input(input):
    split_index = input.index('')
    raw_dots = input[:split_index]
    dots = []
    for dot in raw_dots:
        split_dot = dot.split(',')
        dots.append([int(split_dot[0]), int(split_dot[1])])
    raw_instructions = input[split_index + 1:]
    instructions = []
    for instruction in raw_instructions:
        split_instruction = instruction.split('=')
        instructions.append(
            (split_instruction[0][-1], int(split_instruction[1])))
    return dots, instructions


def count_dots(input):
    dots, instructions = split_input(input)
    for fold in instructions[:1]:
        fold_paper(dots, fold)
    return len(dots)


def fold_paper(dots, fold):
    axis, number = fold
    to_delete = []
    for i, dot in enumerate(dots):
        if axis == 'y':
            if dot[1] == number:
                to_delete.append(i)
            if dot[1] > number:
                new_y = dot[1] - (dot[1] - number) * 2
                if [dot[0], new_y] in dots:
                    to_delete.append(i)
                else:
                    dot[1] = new_y
        if axis == 'x':
            if dot[0] == number:
                to_delete.append(i)
            if dot[0] > number:
                new_x = dot[0] - (dot[0] - number) * 2
                if [new_x, dot[1]] in dots:
                    to_delete.append(i)
                else:
                    dot[0] = new_x

    delete_dots(dots, to_delete)


def delete_dots(dots, to_delete):
    for i, dot_index in enumerate(to_delete):
        del dots[dot_index - i]


def display_dots(dots):
    width = 0
    height = 0
    for dot in dots:
        width = max(dot[0] + 1, width)
        height = max(dot[1] + 1, height)

    for i in range(0, height):
        row = []
        for j in range(0, width):
            row.append('#' if [j, i] in dots else '.')
        print(row)


print(count_dots(input))

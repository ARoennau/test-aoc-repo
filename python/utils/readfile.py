from typing import List, Tuple

def readfile_ints(filename: str) -> List[int]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    input = list(map(lambda str: int(str.replace('\n', '')), lines))
    return input


def readfile_string(filename: str) -> List[str]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    input = list(map(lambda str: str.replace('\n', ''), lines))
    return input


def readfile_bingo(filename: str) -> Tuple[List[int], List[List[int]]]:
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    input = list(map(lambda str: str.replace('\n', ''), lines))
    numbers = list(map(lambda str: int(str), input[0].split(',')))

    boards = []
    current_board = []
    for i in range(2, len(input)):
        if input[i] == '':
            boards.append(current_board)
            current_board = []
            continue
        filtered_row = list(filter(lambda str: str != '', input[i].split(' ')))
        current_board.append(list(map(lambda str: int(str), filtered_row)))

    boards.append(current_board)
    return numbers, boards


def readfile_line_segments(filename: str) -> List[Tuple[Tuple[int]]]:
    input = readfile_string(filename)
    line_segments = []

    for line in input:
        split_line = line.split(' -> ')
        line_segment = (tuple(map(lambda str: int(str), split_line[0].split(
            ','))), tuple(map(lambda str: int(str), split_line[1].split(','))))
        line_segments.append(line_segment)
    return line_segments

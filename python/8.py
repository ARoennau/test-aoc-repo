import sys
from utils.readfile import readfile_bingo

if len(sys.argv) < 2:
    print('No file provided')
    exit()

numbers, boards = readfile_bingo(f'{sys.argv[1]}.txt')


def generate_memo_list(num_boards):
    result = []
    for _ in range(0, num_boards):
        result.append([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    return result


def bingo(numbers, boards):
    # counts of found numbers in each row and column
    memo = generate_memo_list(len(boards))
    value = 0
    number_list = []
    for number in numbers:
        number_list.append(number)
        value = check_numbers(number_list, boards, memo)
        if value > 0:
            return value

    return value


def check_numbers(numbers, boards, memo):
    number = numbers[-1]
    delete_boards = []
    for i, board in enumerate(boards):
        row, col = find_number(number, board)
        if row != -1:
            board_memo = memo[i]
            board_memo[0][row] += 1
            board_memo[1][col] += 1

            if board_memo[0][row] == 5 or board_memo[1][col] == 5:
                if len(boards) > 1:
                    delete_boards.append(i)
                else:
                    return sum_board(board, numbers) * number

    for offset, index in enumerate(delete_boards):
        del(boards[index - offset])
        del(memo[index - offset])
    return 0


def find_number(number, board):
    for row_index, row in enumerate(board):
        for col_index, value in enumerate(row):
            if value == number:
                return row_index, col_index
    return -1, -1


def sum_board(board, numbers):
    total = 0
    for row in board:
        for number in row:
            if number not in numbers:
                total += number
    return total


print(bingo(numbers, boards))

# AdventOfCode/2024/day_06.py

from aocd import get_data
from itertools import cycle

DIRECTIONS = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
TEST_DATA = open("./test_input/day_06.txt", "r").read()
RAW_DATA = get_data(day=6, year=2024)


def parse_data(arr):
    return [[i for i in line] for line in arr.split("\n")]


class guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = next(DIRECTIONS)

    def is_move_valid(self, x, y, board):
        if x >= len(board[0]) or y >= len(board):
            return 0

        if board[y][x] == "#":
            return 2
        return 1

    def move(self, board):
        x, y = self.x, self.y
        new_x, new_y = (
            x + self.direction[0],
            y + self.direction[1],
        )
        valid_move = self.is_move_valid(new_x, new_y, board)
        if valid_move == 1:
            board[y][x] = "X"
            self.y = new_y
            self.x = new_x
            board[self.y][self.x] = "^"
        elif valid_move == 2:
            self.direction = next(DIRECTIONS)
        else:
            return 0

        return 1


def find_guard(board):
    for y, row in enumerate(board):
        if "^" in row:
            return row.index("^"), y


def print_board(board):
    for row in board:
        print("".join(row))


def main():
    board = parse_data(RAW_DATA)
    x, y = find_guard(board)
    npc = guard(x, y)

    while npc.move(board) != 0:
        next

    print(sum(row.count("X") for row in board) + 1)


main()

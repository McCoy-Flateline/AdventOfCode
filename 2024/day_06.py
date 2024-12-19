# AdventOfCode/2024/day_06.py

from aocd import get_data
from typing import List, Tuple

DIRECTIONS: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
TEST_DATA = open("./test_input/day_07.txt", "r").read()
RAW_DATA = get_data(day=6, year=2024)


def parse_data(arr):
    return


class guard:
    def __init__(self, x, y):
        self.location = tuple(x, y)
        self.direction = 0

    def move():
        return

    def is_move_valid():
        return

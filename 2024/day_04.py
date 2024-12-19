# AdventOfCode/2024/day_04.py

from aocd import get_data
from typing import List, Tuple

DIRECTIONS: List[Tuple[int, int]] = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),  # Horizontal & Vertical
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),  # Diagonal
]

CORNER_PATTERNS = {"MMSS", "MSSM", "SSMM", "SMMS"}


def parse_input(raw: str) -> List[List[str]]:
    return [list(line) for line in raw.strip().split("\n")]


def is_in_bounds(x: int, y: int, rows: int, cols: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols


def search_in_direction(
    grid: List[List[str]], word: str, x: int, y: int, dir_x: int, dir_y: int
) -> bool:
    for index, char in enumerate(word):
        new_x, new_y = x + dir_x * index, y + dir_y * index
        if (
            not is_in_bounds(new_x, new_y, len(grid), len(grid[0]))
            or grid[new_x][new_y] != char
        ):
            return False
    return True


def count_word(grid: List[List[str]], word: str) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:
                for dir_x, dir_y in DIRECTIONS:
                    if search_in_direction(grid, word, x, y, dir_x, dir_y):
                        count += 1
    return count


def x_mass_search(grid: List[List[str]]) -> int:
    count = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            if grid[x][y] != "A":
                continue
            corners = (
                grid[x - 1][y - 1]
                + grid[x - 1][y + 1]
                + grid[x + 1][y + 1]
                + grid[x + 1][y - 1]
            )
            if corners in CORNER_PATTERNS:
                count += 1
    return count


data = parse_input(get_data(day=4, year=2024))

print(f"Count of XMAS: {count_word(data, "XMAS")}")
print(f"X-MAS count: {x_mass_search(data)}")

# AdventOfCode/2024/day_02/py

from aocd import get_data
from typing import List

TEST_DATA = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def parse_input(raw: str) -> List[List[int]]:
    return [list(map(int, x.split())) for x in raw.split("\n")]


def is_safe(arr) -> bool:
    increase = all(
        arr[i] < arr[i + 1] and arr[i] + 3 >= arr[i + 1] for i in range(0, len(arr) - 1)
    )
    decrease = all(
        arr[i] > arr[i + 1] and arr[i] - 3 <= arr[i + 1] for i in range(0, len(arr) - 1)
    )
    return increase or decrease


def is_safe_damp(arr) -> bool:
    return any(is_safe(arr[:i] + arr[i + 1 :]) for i in range(len(arr)))


data = parse_input(get_data(day=2, year=2024))
print(f"Number of safe report: {sum(1 for x in data if is_safe(x))}")
print(f"Number of safe dampener reports: {sum(1 for x in data if is_safe_damp(x))}")

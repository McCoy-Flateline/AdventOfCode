# AdventOfCode/2024/day_07.py

from aocd import get_data
from math import log10

from typing import List


TEST_DATA = open("./test_input/day_07.txt", "r").read()
RAW_DATA = get_data(day=7, year=2024)


def parse_input(raw: str) -> List[List[int]]:
    data = raw.split("\n")
    return [list(map(int, line.replace(":", "").split())) for line in data]


def is_tractable(target: int, numbers: List[int], allow_concat: bool = True) -> bool:
    *head, last_number = numbers
    if not head:
        return last_number == target
    full, remainder = divmod(target, last_number)
    if is_tractable(full, head, allow_concat) and remainder == 0:
        return True
    if (
        allow_concat
        and endswith(target, last_number)
        and is_tractable(target // (10 ** digits(last_number)), head, allow_concat)
    ):
        return True
    return is_tractable(target - last_number, head, allow_concat)


def digits(n) -> int:
    return int(log10(n)) + 1


def endswith(a: int, b: int) -> bool:
    return (a - b) % 10 ** digits(b) == 0


data = parse_input(RAW_DATA)

part_1 = 0
for line in data:
    target, *numbers = line
    if is_tractable(target, numbers, False):
        part_1 += target

part_2 = 0
for line in data:
    target, *numbers = line
    if is_tractable(target, numbers, False):
        part_2 += target
    elif is_tractable(target, numbers):
        part_2 += target

print(f"Calibration results: {part_1}\nConcat calibration results: {part_2}")

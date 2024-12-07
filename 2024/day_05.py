# AdventOfCode/2024/day5/py

from aocd import get_data
from typing import List, Tuple
from functools import cmp_to_key

TEST_DATA = open("./test_input/day_05.txt", "r").read()
RAW_DATA = get_data(day=5, year=2024)


def parse_input(raw: str) -> Tuple[List[Tuple[int]], List[List[int]]]:
    rules = []
    pages = []
    for x in raw.split("\n"):
        if "|" in x:
            rules.append(tuple(map(int, x.split("|"))))
        elif x:
            pages.append(list(map(int, x.split(","))))

    return rules, pages


def print_order(rules, pages: List[List[int]]) -> int:
    mid_sum = 0

    for page in pages:
        if all(
            page.index(r1) < page.index(r2)
            for r1, r2 in rules
            if r1 in page and r2 in page
        ):
            mid_sum += page[int((len(page) - 1) / 2)]

    return mid_sum


def correct_order(rules: List[Tuple[int]], pages: List[List[int]]) -> int:
    mid_sum = 0

    for page in pages:
        if any(
            page.index(r1) > page.index(r2)
            for r1, r2 in rules
            if r1 in page and r2 in page
        ):
            corrected = sorted(
                page, key=cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))
            )
            mid_sum += corrected[int((len(corrected) - 1) / 2)]

    return mid_sum


rules, pages = parse_input(RAW_DATA)
mid_sum = print_order(rules, pages)
correct_sum = correct_order(rules, pages)

print(f"Initial sum is {mid_sum}\nCorrected sum is: {correct_sum}")

# AdventOfCode/2024/day_03.py

from aocd import get_data
import re
import math

TEST_DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
TEST_DATA_2 = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)


def multiply(arr) -> int:
    return sum(math.prod(map(int, re.findall(r"\d+", item))) for item in arr)


mul_pattern = r"mul\([\d]*,[\d]*\)"

raw_data = get_data(day=3, year=2024)
data = re.findall(mul_pattern, raw_data)

print(f"Total is: {multiply(data)}")

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

split_data = re.split(f"({do_pattern}|{dont_pattern})", raw_data)

skip = False
total = 0

for x in split_data:
    if re.match(do_pattern, x):
        skip = False
    elif re.match(dont_pattern, x):
        skip = True
    elif not skip:
        total += multiply(re.findall(mul_pattern, x))

print(f"New Total is: {total}")

# AdventOfCode/2024/day_01/py

from aocd import get_data
import re
import math

raw_data = get_data(day=1, year=2024)
left_list, right_list = sorted(map(int, re.split("   |\n", raw_data)[::2])), sorted(
    map(int, re.split("   |\n", raw_data)[1::2])
)

dif = 0
similarity_score = 0

for x, y in zip(left_list, right_list):
    dist = (x - y) ** 2
    dif = dif + math.sqrt(dist)

print(f"Euclidean distance is {dif}")

for x in left_list:
    count = right_list.count(x)
    similarity_score = similarity_score + (x * count)

print(f"Similarity score is: {similarity_score}")

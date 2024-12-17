# AoC 2024 Day 8

from util import *
from collections import defaultdict

# Part 1

with (open_input(8) as f):
    lines = f.readlines()

    ylen, xlen = 50, 50

    antennas = defaultdict(list)
    for i in range(ylen):
        for j in range(len(lines[i])):
            if (fr := lines[i][j]) != '.':
                antennas[fr].append((j, i))

result_set = set()
for pos_ls in antennas.values():
    np = len(pos_ls)
    for i in range(np - 1):
        for j in range(i + 1, np):
            (p1x, p1y), (p2x, p2y) = pos_ls[i], pos_ls[j]
            dx, dy = p2x - p1x, p2y - p1y
            an1x, an1y, an2x, an2y = p1x - dx, p1y - dy, p2x + dx, p2y + dy
            if 0 <= an1x < xlen and 0 <= an1y < ylen:
                result_set.add((an1x, an1y))
            if 0 <= an2x < xlen and 0 <= an2y < ylen:
                result_set.add((an2x, an2y))

result = len(result_set)

result1(result)

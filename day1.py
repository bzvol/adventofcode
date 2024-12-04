# AoC 2024 Day 1

from util import *

# Part 1

l1, l2 = [], []
with open_input(1) as f:
    for line in f:
        n1, n2 = map(int, line.split())
        l1.append(n1)
        l2.append(n2)

sl1 = sorted(l1)
sl2 = sorted(l2)

result = sum(map(lambda x: abs(x[1] - x[0]), list(zip(sl1, sl2))))

result1(result)

# Part 2

result = sum(map(lambda x: x * l2.count(x), l1))

result2(result)

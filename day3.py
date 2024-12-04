# AoC 2024 Day 3

from util import *
import re
from math import prod

# Part 1


def eval_mul(op): return prod(map(int, op[4:-1].split(',')))


with open_input(3) as f:
    memory = f.read()

ops = re.findall(r"mul\(\d+,\d+\)", memory)
result = sum(map(eval_mul, ops))

result1(result)

# Part 2

ops = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))", memory)

result = 0
do = True
for mul_op, do_op, dont_op in ops:
    if dont_op:
        do = False
    elif do_op:
        do = True
    elif do:
        result += eval_mul(mul_op)

result2(result)

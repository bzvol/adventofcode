# AoC 2024 Day 7

from util import *


# Part 1 & 2

def is_solvable(target: int, ops: list[str], with_concat_op: bool = False) -> bool:
    return ((with_concat_op and int(ops[0] + ops[1]) == target) or
            int(ops[0]) + int(ops[1]) == target or
            int(ops[0]) * int(ops[1]) == target) if len(ops) == 2 \
        else ((with_concat_op and is_solvable(target, [ops[0] + ops[1]] + ops[2:], with_concat_op)) or
              is_solvable(target, [str(int(ops[0]) + int(ops[1]))] + ops[2:], with_concat_op) or
              is_solvable(target, [str(int(ops[0]) * int(ops[1]))] + ops[2:], with_concat_op))


result1_ = 0
result2_ = 0

with open_input(7) as f:
    for line in f.readlines():
        target, *ops = line.split()
        target = int(target[:-1])
        if is_solvable(target, ops):
            result1_ += target
            result2_ += target
        elif is_solvable(target, ops, True):
            result2_ += target

result1(result1_)
result2(result2_)

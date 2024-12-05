# AoC 2024 Day 5

from util import *

# Part 1

def is_valid(update, x, y):
    if x in update and y in update:
        x_index = update.index(x)
        if y not in update[x_index + 1:]:
            return False
    return True

with open_input(5) as f:
    rules = []
    line = f.readline().strip()
    while line:
        rules.append(tuple(map(int, line.split('|'))))
        line = f.readline().strip()

    updates = []
    line = f.readline().strip()
    while line:
        updates.append(list(map(int, line.split(','))))
        line = f.readline().strip()

result = 0

incorrect_updates = []
for i, update in enumerate(updates):
    correct = True
    for x, y in rules:
        if not is_valid(update, x, y):
            correct = False
            incorrect_updates.append(i)
            break
    
    if correct:
        result += update[len(update) // 2]

result1(result)

# Part 2

# I couldn't find out... so this is not my solution :/
# https://www.reddit.com/r/adventofcode/comments/1h71eyz/comment/m0i0nqh/
def reorder(update, rules):
    if len(update) <= 1:
        return update
    
    ls, rs = [], []
    l = update[0]
    for r in update[1:]:
        if (r, l) in rules:
            ls.append(r)
        else:
            rs.append(r)
            
    return reorder(ls, rules) + [l] + reorder(rs, rules)

result = 0

for i in range(len(incorrect_updates)):
    update = updates[incorrect_updates[i]]
    ordered_update = reorder(update, rules)
    result += ordered_update[len(ordered_update) // 2]

result2(result)

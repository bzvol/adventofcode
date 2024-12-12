# AoC 2024 Day 6

from util import *

# Part 1

with open_input(6) as f:
    pos_map = f.readlines()
    x_max, y_max = len(pos_map[0]) - 1, len(pos_map) - 1
    obstacles = [(j, i) for i in range(len(pos_map)) for j in range(len(pos_map[i])) if pos_map[i][j] == '#']
    guard_pos = [(j, i) for i in range(len(pos_map)) for j in range(len(pos_map[i])) if pos_map[i][j] == '^'][0]

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_idx = 0
x_dir, y_dir = dirs[dir_idx]

guard_pos_set = {guard_pos}
while True:
    guard_pos_set.add(guard_pos)
    x, y = guard_pos
    nx, ny = x + x_dir, y + y_dir

    if nx < 0 or nx > x_max or ny < 0 or ny > y_max:
        break

    if (nx, ny) in obstacles:
        dir_idx = (dir_idx + 1) % 4
        x_dir, y_dir = dirs[dir_idx]
        continue

    guard_pos = (nx, ny)

result = len(guard_pos_set)

result1(result)

# Part 2

result = 0

result2(result)

# AoC 2024 Day 9

from util import *
from time import time

# Part 1

with open_input(9) as f:
    disk_str = f.read()

start_time = time()

len_disk_str = len(disk_str)

disk = []
compacted_disk_length = 0
for i in range(0, len_disk_str, 2):
    block_id, block_length = i // 2, int(disk_str[i])
    disk += [block_id] * block_length
    compacted_disk_length += block_length

    if i + 1 < len_disk_str and (space_length := int(disk_str[i + 1])) > 0:
        disk.append(-space_length)

to_be_moved = [el for el in disk[compacted_disk_length:] if el >= 0]
n_tbm = len(to_be_moved)
n_moved = 0

last_fs_idx = -1
last_n_moved = 1
while n_moved < n_tbm:
    for i in range(last_fs_idx + last_n_moved, compacted_disk_length):
        if disk[i] < 0:
            last_fs_idx = i
            break

    last_n_moved = -disk[last_fs_idx]

    move_to = to_be_moved[-n_moved-last_n_moved:-n_moved] if n_moved > 0 else to_be_moved[-n_moved-last_n_moved:]
    disk[last_fs_idx:last_fs_idx+1] = move_to[::-1]

    n_moved += last_n_moved

for i in range(compacted_disk_length):
    if disk[i] < 0:
        print(i)

result = 0

result1(result)

# Part 2

result = 0

result2(result)

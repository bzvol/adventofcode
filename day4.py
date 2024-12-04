# AoC 2024 Day 4

from util import *

# Part 1

with open_input(4) as f:
    inp = f.readlines()

width = len(inp[0])
height = len(inp)
xmas = 'XMAS'
samx = 'SAMX'

result = 0
for i in range(height):
    for j in range(width):
        if j < width - 3 and inp[i][j:j+4] == xmas:  # Right
            result += 1
        if j > 2 and inp[i][j-3:j+1] == samx:  # Left
            result += 1
        if i < height - 3 and (inp[i][j] + inp[i + 1][j] + inp[i + 2][j] + inp[i + 3][j]) == xmas:  # Down
            result += 1
        if i > 2 and (inp[i - 3][j] + inp[i - 2][j] + inp[i - 1][j] + inp[i][j]) == samx:  # Up
            result += 1
        if j < width - 3 and i < height - 3 and (inp[i][j] + inp[i + 1][j + 1] + inp[i + 2][j + 2] + inp[i + 3][j + 3]) == xmas: # Down-right
            result += 1
        if j > 2 and i < height - 3 and (inp[i][j] + inp[i + 1][j - 1] + inp[i + 2][j - 2] + inp[i + 3][j - 3]) == xmas: # Down-left
            result += 1
        if j > 2 and i > 2 and (inp[i][j] + inp[i - 1][j - 1] + inp[i - 2][j - 2] + inp[i - 3][j - 3]) == xmas: # Up-left
            result += 1
        if j < width - 3 and i > 2 and (inp[i][j] + inp[i - 1][j + 1] + inp[i - 2][j + 2] + inp[i - 3][j + 3]) == xmas: # Up-right
            result += 1


result1(result)

# Part 2

mas = 'MAS'
sam = 'SAM'

result = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        l1 = inp[i - 1][j - 1] + inp[i][j] + inp[i + 1][j + 1]
        l2 = inp[i + 1][j - 1] + inp[i][j] + inp[i - 1][j + 1]
        if (l1 == mas or l1 == sam) and (l2 == mas or l2 == sam):
            result += 1

result2(result)

# Aaaah this was not my nicest code...

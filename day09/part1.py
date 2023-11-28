#!/usr/bin/env python3

import argparse
from rope import GenerateGrid, ProcessLines, MoveCloser
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

moves = ProcessLines(lines)

grid = GenerateGrid(moves)

head = (0, 0)
tail = (0, 0)

grid.Set(tail, True)

for move in moves:
    head = (head[0] + move[0], head[1] + move[1])
    tail = MoveCloser(head, tail)
    grid.Set(tail, True)

count = 0
for x in range(len(grid.grid)):
    for y in range(len(grid.grid[x])):
        if grid.grid[x][y] == True:
            count += 1
print("Count:", count)

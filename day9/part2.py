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

knots = [ (0, 0) for x in range(10) ]

grid.Set((0, 0), True)

for move in moves:
    knots[0] = (knots[0][0] + move[0], knots[0][1] + move[1])
    for i in range(1,len(knots)):
        knots[i] = MoveCloser(knots[i-1], knots[i])
    grid.Set(knots[9], True)

count = 0
for x in range(len(grid.grid)):
    for y in range(len(grid.grid[x])):
        if grid.grid[x][y] == True:
            count += 1
print("Count:", count)

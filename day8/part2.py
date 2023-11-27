#!/usr/bin/env python3

import argparse
from forest import LoadGrid, ViewScore
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

grid = LoadGrid(lines)

maximum = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        score = ViewScore(grid, row, column)
        if score > maximum:
            maximum = score

print("Maximum Score:", maximum)

#!/usr/bin/env python3

import argparse
from forest import LoadGrid, IsVisible
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

grid = LoadGrid(lines)

visible = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if IsVisible(row, column):
            visible += 1

print("Visible:", visible)

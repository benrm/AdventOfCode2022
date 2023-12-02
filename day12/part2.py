#!/usr/bin/env python3

import argparse
from grid import LoadGrid
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = args.input.readlines()

grid = LoadGrid(lines)
grid.start.visited = False

lowest = []
for row in grid.grid:
    for cell in row:
        if cell.value == 0:
            lowest.append(cell.point)

minimum = None
for point in lowest:
    new = grid.Copy()
    new.start = new.Get(point)
    new.start.visited = True
    path = new.Search()
    if len(path) > 0 and (minimum is None or len(path)-1 < minimum):
        minimum = len(path)-1

print("Distance:", minimum)

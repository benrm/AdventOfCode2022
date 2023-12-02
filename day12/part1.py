#!/usr/bin/env python3

import argparse
from grid import LoadGrid
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = args.input.readlines()

grid = LoadGrid(lines)

print("Distance:", len(grid.Search())-1)

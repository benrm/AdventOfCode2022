#!/usr/bin/env python3

import argparse
from cave import GenerateCave
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

cave = GenerateCave(args.input.readlines())
cave.Fill(floor=True)

total = 0
for column in cave.grid:
    for cell in column:
        if cell == "sand":
            total += 1
print("Total:", total)

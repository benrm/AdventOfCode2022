#!/usr/bin/env python3

import argparse
import geometry
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
parser.add_argument("--row", "-r", default=10, type=int)
args = parser.parse_args()

rows = geometry.Parse(args.input.readlines())

min_x = 0
max_x = 0
for row in rows:
    if row["sensor"].x - row["distance"] < min_x:
        min_x = row["sensor"].x - row["distance"]
    if row["sensor"].x + row["distance"] > max_x:
        max_x = row["sensor"].x + row["distance"]

beacons = { row["beacon"] for row in rows }
sensors = { row["sensor"] for row in rows }

total = 0
for x in range(min_x, max_x+1):
    point = geometry.Point(x, args.row)
    if point not in beacons and point not in sensors:
        invalid = False
        for row in rows:
            if geometry.ManhattanDistance(row["sensor"], point) <= row["distance"]:
                invalid = True
                break
        if invalid:
            total += 1
print("Total:", total)

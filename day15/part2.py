#!/usr/bin/env python3

import argparse
import geometry
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
parser.add_argument("--max", "-m", default=20, type=int)
args = parser.parse_args()

rows = geometry.Parse(args.input.readlines())

lines = []
for row in rows:
    left = geometry.Point(row["sensor"].x - row["distance"] - 1, row["sensor"].y)
    top = geometry.Point(row["sensor"].x, row["sensor"].y + row["distance"] + 1)
    right = geometry.Point(row["sensor"].x + row["distance"] + 1, row["sensor"].y)
    bottom = geometry.Point(row["sensor"].x, row["sensor"].y - row["distance"] - 1)
    lines.append(geometry.CreateLine(left, top))
    lines.append(geometry.CreateLine(top, right))
    lines.append(geometry.CreateLine(right, bottom))
    lines.append(geometry.CreateLine(bottom, left))

intersection = None
for i in range(len(lines)):
    for j in range(1, len(lines)):
        if i == j:
            continue
        point = geometry.Intersect(lines[i], lines[j])
        if point is not None:
            invalid = False
            for row in rows:
                if geometry.ManhattanDistance(row["sensor"], point) <= row["distance"]:
                    invalid = True
                    break
            if not invalid and 0 <= point.x and point.x <= args.max and 0 <= point.y and point.y <= args.max:
                intersection = point
                break
    if intersection is not None:
        break
if intersection is not None:
    print("Tuning Frequency:", int(intersection.x * 4000000 + intersection.y))
else:
    print("No Tuning Frequency")

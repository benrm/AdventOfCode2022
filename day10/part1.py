#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

cycle = 1
register = 1

total = 0

for line in lines:
    words = line.split()
    if words[0] == "noop":
        cycle += 1
        if (cycle - 20) % 40 == 0:
            total += cycle * register
    elif words[0] == "addx":
        cycle += 1
        if (cycle - 20) % 40 == 0:
            total += cycle * register
        cycle += 1
        register += int(words[1])
        if (cycle - 20) % 40 == 0:
            total += cycle * register
    else:
        raise Exception("Unknown command: %s" % (words[0]))

print("Total:", total)

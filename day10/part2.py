#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

cycle = 1
register = 1

def PrintPixel(cycle, register):
    if (cycle - 1) % 40 >= register - 1 and (cycle - 1) % 40 <= register + 1:
        print("#", end="")
    else:
        print(".", end="")
    if (cycle - 1) % 40 == 39:
        print("")

for line in lines:
    words = line.split()
    if words[0] == "noop":
        PrintPixel(cycle, register)
        cycle += 1
    elif words[0] == "addx":
        PrintPixel(cycle, register)
        cycle += 1
        PrintPixel(cycle, register)
        cycle += 1
        register += int(words[1])
    else:
        raise Exception("Unknown command: %s" % (words[0]))

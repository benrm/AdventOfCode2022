#!/usr/bin/env python3

import argparse
from packet import ParsePacket, ComparePackets
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = args.input.readlines()

total = 0
i = 0
pair = 1
while i < len(lines):
    left = ParsePacket(lines[i])
    right = ParsePacket(lines[i+1])
    if ComparePackets(left, right) > 0:
        print("Packet %d: Correct" % pair)
        total += pair
    else:
        print("Packet %d: Incorrect" % pair)
    i += 3
    pair += 1

print("Total:", total)

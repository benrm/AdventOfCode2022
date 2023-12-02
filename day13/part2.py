#!/usr/bin/env python3

import argparse
from packet import ParsePacket, ComparePackets
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType("r"))
args = parser.parse_args()

lines = args.input.readlines()

class Packet:
    def __init__(self, value, divider=False):
        self.value = value
        self.divider = divider

packets = []
for line in lines:
    if line.strip() == "":
        continue
    packets.append(Packet(ParsePacket(line)))
packets.append(Packet([[2]], divider=True))
packets.append(Packet([[6]], divider=True))

i = len(packets)-1
while i > 0:
    j = i-1
    while j >= 0:
        if ComparePackets(packets[i].value, packets[j].value) == 1:
            tmp = packets[i]
            packets[i] = packets[j]
            packets[j] = tmp
        j -= 1
    i -= 1

product = 1
found = 0
i = 0
while i < len(packets):
    if packets[i].divider:
        product *= i+1
        found += 1
        if found == 2:
            break
    i += 1

print("Product:", product)

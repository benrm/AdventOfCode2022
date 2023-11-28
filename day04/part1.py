#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

total = 0
for line in args.input.readlines():
    ab, cd = line.strip().split(',')
    a, b = ab.split('-')
    c, d = cd.split('-')
    if (int(a) <= int(c) and int(b) >= int(d)) or (int(c) <= int(a) and int(d) >= int(b)):
        total += 1

print("Total: " + str(total))

#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

priorities = {}
for c in range(ord('a'), ord('z') + 1):
    priorities[chr(c)] = c - ord('a') + 1
for c in range(ord('A'), ord('Z') + 1):
    priorities[chr(c)] = c - ord('A') + 27

total = 0
lines = args.input.readlines()
for i in range(0, len(lines), 3):
    a = set(lines[i].strip())
    b = set(lines[i+1].strip())
    c = set(lines[i+2].strip())
    for v in a&b&c:
        total += priorities[v]

print("Total: " + str(total))

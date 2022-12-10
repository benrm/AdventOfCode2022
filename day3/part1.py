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
for line in args.input.readlines():
    line.strip()
    i = int(len(line)/2)
    a = set(line[0:i])
    b = set(line[i:len(line)])
    for v in a&b:
        total += priorities[v]

print("Total: " + str(total))

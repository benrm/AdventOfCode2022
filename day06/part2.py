#!/usr/bin/python3
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

line = args.input.readline()
i = 0
while i+13 < len(line):
    s = set(line[i:i+14])
    if len(s) == 14:
        print("i: " + str(i+14))
        sys.exit()
    i += 1

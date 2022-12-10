#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

result = []
total = 0
for line in args.input.readlines():
    line.strip()
    themChar, usChar = line.split()
    themInt, usInt, score = 0, 0, 0

    if themChar == 'A':
        themInt = 1
    elif themChar == 'B':
        themInt = 2
    elif themChar == 'C':
        themInt = 3

    if usChar == 'X':
        usInt = 1
    elif usChar == 'Y':
        usInt = 2
    elif usChar == 'Z':
        usInt = 3

    if themInt == usInt:
        score = usInt + 3
    elif themInt - 1 == usInt % 3:
        score = usInt
    elif usInt - 1 == themInt % 3:
        score = usInt + 6

    total += score

print("Score: " + str(total))

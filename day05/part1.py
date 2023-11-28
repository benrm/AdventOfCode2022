#!/usr/bin/python3
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

lines = []
c = True
while c:
    line = args.input.readline().strip()
    if line == "":
        c = False
    else:
        lines.append(line)
lines.reverse()

stacks = []
for line in lines:
    stacks.append([])

for line in lines:
    i = 1
    stack = 0
    while i < len(line):
        if line[i] != " ":
            stacks[stack].append(line[i])
        i += 4
        stack += 1

c = True
r = re.compile('move (\d+) from (\d+) to (\d+)')
while c:
    command = args.input.readline().strip()
    if command == "":
        c = False
    else:
        values = [ int(x) for x in r.match(command).groups() ]
        for i in range(0,values[0]):
            v = stacks[values[1]-1].pop()
            stacks[values[2]-1].append(v)

output = ""
for stack in stacks:
    output += stack.pop()

print("Output: " + output)

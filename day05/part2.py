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
        count, source, dest = [ int(x) for x in r.match(command).groups() ]
        source -= 1
        dest -= 1
        v = stacks[source][len(stacks[source])-count:len(stacks[source])]
        stacks[source] = stacks[source][0:len(stacks[source])-count]
        stacks[dest].extend(v)

output = ""
for stack in stacks:
    output += stack.pop()

print("Output: " + output)

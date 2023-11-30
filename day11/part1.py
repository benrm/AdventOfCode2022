#!/usr/bin/env python3

import argparse
from monkey import ProcessLines
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
parser.add_argument("--rounds", "-r", type=int)
args = parser.parse_args()

monkeys = {}

all_lines = args.input.readlines()

monkeys = ProcessLines(all_lines)

names = sorted(monkeys.keys())

for i in range(args.rounds):
    for name in names:
        for item in monkeys[name].items:
            item = monkeys[name].operation(item)
            item = item // 3
            if item % monkeys[name].test == 0:
                target = monkeys[name].if_true
            else:
                target = monkeys[name].if_false
            monkeys[target].items.append(item)
        monkeys[name].inspected += len(monkeys[name].items)
        monkeys[name].items = []

inspected = { monkeys[name].inspected for name in names }
greatest = max(inspected)
inspected.remove(greatest)
second_greatest = max(inspected)

print("Monkey Business:", greatest * second_greatest)

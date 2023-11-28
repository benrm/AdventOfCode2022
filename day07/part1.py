#!/usr/bin/env python3

import argparse
from fake_file import FakeFile, LoadFilesystem
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

root = LoadFilesystem(lines)

total = 0
for _dir in root.AllDirs():
    if _dir.Size() < 100000:
        total += _dir.Size()

print("Total:", total)

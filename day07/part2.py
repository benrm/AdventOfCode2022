#!/usr/bin/env python3

import argparse
from fake_file import FakeFile, LoadFilesystem
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

root = LoadFilesystem(lines)

total_available = 70000000
total_desired = 30000000
total_used = root.Size()
need = total_desired - total_available + total_used

choice = None
for _dir in root.AllDirs():
    if _dir.Size() >= need:
        if choice is None or _dir.Size() < choice.Size():
            choice = _dir

print("Size:", choice.Size())

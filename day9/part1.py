#!/usr/bin/env python3

import argparse
from rope import FindBounds
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", "-i", default=sys.stdin, type=argparse.FileType('r'))
args = parser.parse_args()

lines = args.input.readlines()

bounds = FindBounds(lines)

print("Bounds:", bounds)

#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=argparse.FileType())
args = parser.parse_args()

elves = []
elf = []
for line in args.input.readlines():
    if not line.strip():
        if len(elf) > 0:
            elves.append(elf)
        elf = []
    else:
        elf.append(int(line.strip()))
if len(elf) > 0:
    elves.append(elf)

index = [0, 0, 0]
most_calories = [0, 0, 0]
i = 0
for elf in elves:
    calories = 0
    for food in elf:
        calories += food
        if calories > most_calories[0]:
            most_calories[2], index[2] = most_calories[1], index[1]
            most_calories[1], index[1] = most_calories[0], index[0]
            most_calories[0], index[0] = calories, i
        elif calories > most_calories[1]:
            most_calories[2], index[2] = most_calories[1], index[1]
            most_calories[1], index[1] = calories, i
        elif calories > most_calories[2]:
            most_calories[2], index[2] = calories, i
    i += 1

print("Index: " + str(index))
print("Calories: " + str(most_calories))
print("Sum of Calories: " + str(sum(most_calories)))

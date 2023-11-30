import re

class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0

    def Print(self):
        print("Monkey %s: %s" % (self.name, self.items))

name_re = re.compile("Monkey ([\d]+):")
item_re = re.compile("(\d+)")
operation_re = re.compile("Operation: new = (.*)")
divisible_re = re.compile("divisible by ([\d]+)")
throw_re = re.compile("If (?:true|false): throw to monkey ([\d]+)")

def generateAdditionOperation(value):
    return lambda old : old + value

def generateMultiplicationOperation(value):
    return lambda old : old * value

def ProcessLines(all_lines):
    monkeys = {}
    while len(all_lines) > 0:
        lines = all_lines[0:6]
        all_lines = all_lines[7:]

        matches = name_re.search(lines[0])
        if matches:
            name = matches[1]
        else:
            raise Exception("Couldn't handle name")

        items = [ int(item) for item in item_re.findall(lines[1]) ]

        matches = operation_re.search(lines[2])
        if matches:
            operators = matches[1].split()
            if operators[1] == "+":
                if operators[2] == "old":
                    operation = lambda old : old + old
                else:
                    operation = generateAdditionOperation(int(operators[2]))
            elif operators[1] == "*":
                if operators[2] == "old":
                    operation = lambda old : old * old
                else:
                    operation = generateMultiplicationOperation(int(operators[2]))
            else:
                raise Exception("Unhandled operation: %s" % (operators[1]))
        else:
            raise Exception("Couldn't handle operation")

        matches = divisible_re.search(lines[3])
        if matches:
            divisible = int(matches[1])
        else:
            raise Exception("Couldn't handle test")

        matches = throw_re.search(lines[4])
        if matches:
            if_true = matches[1]
        else:
            raise Exception("Couldn't handle if true")

        matches = throw_re.search(lines[5])
        if matches:
            if_false = matches[1]
        else:
            raise Exception("Couldn't handle if false")

        monkeys[name] = Monkey(name, items, operation, divisible, if_true, if_false)

    return monkeys

import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"Point(x:{self.x},y:{self.y})"

class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

def CreateLine(a, b):
    slope = (a.y - b.y)/(a.x - b.x)
    intercept = -1 * (slope * a.x - a.y)
    return Line(slope, intercept)

def Intersect(a, b):
    if a.slope == b.slope:
        return None
    x = (a.intercept - b.intercept)/(b.slope - a.slope)
    y = a.slope * x + a.intercept
    return Point(x, y)

def ManhattanDistance(sensor, beacon):
    return abs(sensor.x-beacon.x) + abs(sensor.y-beacon.y)

sensor_re = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

def Parse(lines):
    rows = []
    for line in lines:
        matches = sensor_re.match(line)
        if not matches:
            raise Exception("Sensor line not correct format")
        sensor = Point(int(matches[1]), int(matches[2]))
        beacon = Point(int(matches[3]), int(matches[4]))
        rows.append({
            "sensor": sensor,
            "beacon": beacon,
            "distance": ManhattanDistance(sensor, beacon)
        })
    return rows

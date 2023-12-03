import re

class Cave:
    def __init__(self, origin=(500, 0)):
        self.grid = []
        self.origin = origin

    def Print(self, left=0, right=-1, top=0, bottom=-1):
        if right == -1 or right > len(self.grid):
            right = len(self.grid)
        if bottom == -1 or bottom > len(self.grid[0]):
            bottom = len(self.grid[0])
        for y in range(top, bottom, 1):
            for x in range(left, right, 1):
                cell = self.grid[x][y]
                if cell == "rock":
                    print("X", end="")
                elif cell == "empty":
                    print(" ", end="")
                else:
                    print("s", end="")
            print("")

    def Fill(self, floor=False):
        while True:
            point = self.origin
            if self.grid[point[0]][point[1]] != "empty":
                break
            while True:
                try:
                    if point[1]+1 >= len(self.grid[0]) and floor:
                        self.grid[point[0]][point[1]] = "sand"
                        break
                    elif self.grid[point[0]][point[1]+1] == "empty":
                        point = (point[0], point[1]+1)
                    elif self.grid[point[0]-1][point[1]+1] == "empty":
                        point = (point[0]-1, point[1]+1)
                    elif self.grid[point[0]+1][point[1]+1] == "empty":
                        point = (point[0]+1, point[1]+1)
                    else:
                        self.grid[point[0]][point[1]] = "sand"
                        break
                except IndexError:
                    return

point_re = re.compile("(\d+),(\d+)")

def GenerateCave(lines):
    cave = Cave()
    paths = []
    for line in lines:
        points = [ (int(point[0]), int(point[1])) for point in point_re.findall(line) ]
        paths.append(points)
    (max_x, max_y) = cave.origin
    for path in paths:
        for point in path:
            if point[0] > max_x:
                max_x = point[0]
            if point[1] > max_y:
                max_y = point[1]
    max_y += 1
    max_x = 500 + max_y if 500 + max_y > max_x else max_x
    cave.grid = [ [ "empty" for i in range(max_y+1) ] for j in range(max_x+1) ]
    for path in paths:
        i = 1
        while i < len(path):
            if path[i][0] == path[i-1][0]:
                x = path[i][0]
                if path[i][1] > path[i-1][1]:
                    r = range(path[i-1][1],path[i][1]+1)
                else:
                    r = range(path[i][1], path[i-1][1]+1)
                for y in r:
                    cave.grid[x][y] = "rock"
            elif path[i][1] == path[i-1][1]:
                y = path[i][1]
                if path[i][0] > path[i-1][0]:
                    r = range(path[i-1][0],path[i][0]+1)
                else:
                    r = range(path[i][0], path[i-1][0]+1)
                for x in r:
                    cave.grid[x][y] = "rock"
            else:
                raise Exception("Line neither vertical nor horizontal: (%s and %s)" % path[i-1], path[i])
            i += 1
    return cave

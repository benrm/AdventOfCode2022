char_array = "abcdefghijklmnopqrstuvwxyz"
char_map = {}
for i in range(len(char_array)):
    char_map[char_array[i]] = i

class Cell:
    def __init__(self, point, value, grid, visited=False):
        self.point = point
        self.value = value
        self.grid = grid
        self.visited = visited
        self.previous = None

    def GetNeighbors(self):
        neighbors = []
        if self.point[0] > 0:
            neighbors.append(self.grid.Get((self.point[0]-1, self.point[1])))
        if self.point[1] > 0:
            neighbors.append(self.grid.Get((self.point[0], self.point[1]-1)))
        if self.point[0] < self.grid.Width()-1:
            neighbors.append(self.grid.Get((self.point[0]+1, self.point[1])))
        if self.point[1] < self.grid.Height()-1:
            neighbors.append(self.grid.Get((self.point[0], self.point[1]+1)))
        return neighbors

    def Copy(self):
        return Cell(self.point, self.value, None, self.visited)

class Grid:
    def __init__(self):
        self.grid = []
        self.start = None
        self.end = None

    def Get(self, point):
        return self.grid[point[1]][point[0]]

    def Height(self):
        return len(self.grid)

    def Width(self):
        return len(self.grid[0])

    def Copy(self):
        new = Grid()
        new.grid = [ [ cell.Copy() for cell in row ] for row in self.grid ]
        for row in new.grid:
            for cell in row:
                cell.grid = new
        new.start = new.Get(self.start.point)
        new.end = new.Get(self.end.point)
        return new

    def Search(self):
        to_visit = [self.start]
        while len(to_visit) > 0:
            current = to_visit[0]
            to_visit = to_visit[1:]
            for neighbor in current.GetNeighbors():
                if neighbor.visited == False and neighbor.value <= current.value+1:
                    neighbor.visited = True
                    neighbor.previous = current
                    if neighbor == self.end:
                        path = []
                        current = self.end
                        while current is not None:
                            path.append(current)
                            current = current.previous
                        path.reverse()
                        return path
                    to_visit.append(neighbor)
        return []

def LoadGrid(lines):
    grid = Grid()
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            char = lines[y][x]
            point = (x, y)
            if char == "S":
                grid.start = Cell(point, char_map["a"], grid, visited=True)
                row.append(grid.start)
            elif char == "E":
                grid.end = Cell(point, char_map["z"], grid)
                row.append(grid.end)
            elif char == "\n":
                break
            else:
                row.append(Cell(point, char_map[char], grid))
        grid.grid.append(row)
    return grid

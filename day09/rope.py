class Grid:
    def __init__(self, width, height, x_offset, y_offset):
        self.grid = [ [ None for y in range(height) ] for x in range(width) ]
        self.x_offset = x_offset
        self.y_offset = y_offset

    def Get(self, point):
        return self.grid[point[0]+self.x_offset][point[1]+self.y_offset]

    def Set(self, point, value):
        self.grid[point[0]+self.x_offset][point[1]+self.y_offset] = value

    def Print(self):
        print("---")
        for y in range(len(self.grid[0])-1,-1,-1):
            for x in range(len(self.grid)):
                print(self.grid[x][y], end="")
            print()

def ProcessLines(lines):
    moves = []
    for line in lines:
        words = line.split()
        if words[0] == "R":
            move = (1,0)
        elif words[0] == "L":
            move = (-1,0)
        elif words[0] == "U":
            move = (0, 1)
        elif words[0] == "D":
            move = (0, -1)
        else:
            raise Exception("Unknown movement: %s" % (words[0]))
        moves.extend([move]*int(words[1]))
    return moves

def GenerateGrid(moves):
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    curr_x = 0
    curr_y = 0

    for move in moves:
        curr_x += move[0]
        curr_y += move[1]

        if curr_x > max_x:
            max_x = curr_x
        elif curr_x < min_x:
            min_x = curr_x
        elif curr_y > max_y:
            max_y = curr_y
        elif curr_y < min_y:
            min_y = curr_y

    return Grid(max_x - min_x + 1, max_y - min_y + 1, -1 * min_x, -1 * min_y)

def MoveCloser(head, tail):
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return tail
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            return (tail[0], tail[1] + 1)
        elif head[1] < tail[1]:
            return (tail[0], tail[1] - 1)
    elif head[0] > tail[0]:
        if head[1] == tail[1]:
            return (tail[0] + 1, tail[1])
        elif head[1] > tail[1]:
            return (tail[0] + 1, tail[1] + 1)
        elif head[1] < tail[1]:
            return (tail[0] + 1, tail[1] - 1)
    elif head[0] < tail[0]:
        if head[1] == tail[1]:
            return (tail[0] - 1, tail[1])
        elif head[1] > tail[1]:
            return (tail[0] - 1, tail[1] + 1)
        elif head[1] < tail[1]:
            return (tail[0] - 1, tail[1] - 1)
    return tail

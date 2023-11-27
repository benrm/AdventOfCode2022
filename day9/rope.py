class Grid:
    def __init__(self, x, y):
        self.grid = [[False] * y] * x
        return self

    def At(self, x, y):
        return self.grid[x][y]

def FindBounds(lines):
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    curr_x = 0
    curr_y = 0

    for line in lines:
        words = line.split()
        if words[0] == "R":
            curr_x += int(words[1])
            if curr_x > max_x:
                max_x = curr_x
        elif words[0] == "L":
            curr_x -= int(words[1])
            if curr_x < min_x:
                min_x = curr_x
        elif words[0] == "U":
            curr_y += int(words[1])
            if curr_y > max_y:
                max_y = curr_y
        elif words[0] == "D":
            curr_y -= int(words[1])
            if curr_y < min_y:
                min_y = curr_y
        else:
            raise Exception("Unknown movement: %s" % (words[0]))

    return (max_x - min_x, max_y - min_y)

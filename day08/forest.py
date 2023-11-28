def LoadGrid(lines):
    rows = []
    for line in lines:
        columns = []
        for char in line.strip():
            columns.append(int(char))
        rows.append(columns)
    return rows

def IsVisible(grid, row, column):
    if row == 0 or column == 0 or row + 1 == len(grid) or column + 1 == len(grid[row]):
        return True
    visible = True
    for i in range(0, row):
        if grid[i][column] >= grid[row][column]:
            visible = False
            break
    if visible:
        return True
    visible = True
    for i in range(row+1, len(grid)):
        if grid[i][column] >= grid[row][column]:
            visible = False
            break
    if visible:
        return True
    visible = True
    for j in range(0, column):
        if grid[row][j] >= grid[row][column]:
            visible = False
            break
    if visible:
        return True
    for j in range(column+1, len(grid[row])):
        if grid[row][j] >= grid[row][column]:
            return False
    return True

def ViewScore(grid, row, column):
    if row == 0 or column == 0 or row + 1 == len(grid) or column + 1 == len(grid[row]):
        return 0
    visible_above = 0
    for i in range(row-1, -1, -1):
        visible_above += 1
        if grid[i][column] >= grid[row][column]:
            break
    visible_below = 0
    for i in range(row+1, len(grid)):
        visible_below += 1
        if grid[i][column] >= grid[row][column]:
            break
    visible_left = 0
    for j in range(column-1, -1, -1):
        visible_left += 1
        if grid[row][j] >= grid[row][column]:
            break
    visible_right = 0
    for j in range(column+1, len(grid[row])):
        visible_right += 1
        if grid[row][j] >= grid[row][column]:
            break
    return visible_above * visible_below * visible_left * visible_right

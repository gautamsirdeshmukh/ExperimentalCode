def CreateGrid(size):
    rows, cols = size[0], size[1]
    base = []
    for row in range(rows):
        base.append([])
    for row in base:
        for col in range(cols):
            row.append([])
    return base

def PrintGrid(grid):
    for row in grid:
        print(row)
            
size = [int(input('# Rows: ')), int(input('# Cols: '))]
GRID = CreateGrid(size)
PrintGrid(GRID)


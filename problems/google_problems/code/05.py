def check_line(grid, line_idx):
    hist = [0] * 10
    for val in grid[line_idx]:
        if val == 0:
            continue
        hist[val] += 1
        if hist[val] > 1:
            return False
    
    return True

def check_col(grid, col_idx):
    hist = [0] * 10
    values = [grid[i][col_idx] for i in range(9)]

    for val in values:
        if val == 0:
            continue
        hist[val] += 1
        if hist[val] > 1:
            return False

    return True

def check_block(grid, i, j):
    x_block, y_block = int(i/3), int(j/3)
    x_start, y_start = x_block * 3, y_block * 3
    
    values = []
    
    for x in range(3):
        for y in range(3):
            values.append(grid[x_start + x][y_start + y])
            
    hist = [0] * 10
    for val in values:
        if val == 0:
            continue
        hist[val] += 1
        if hist[val] > 1:
            return False
    
    return True

def solve_sdk(grid, last_x, last_y):
    if not check_line(grid, last_x) or not check_col(grid, last_y) or not check_block(grid, last_x, last_y):
        return False
    for x in range(9):
        for y in range(9):
            if grid[x][y] != 0:
                continue
            for val in range(1, 10):
                grid[x][y] = val
                filled = solve_sdk(grid, x, y)
                if not filled:
                    grid[x][y] = 0
                else:
                    break
            if grid[x][y] == 0:
                return False
    return True
    
def print_grid(grid):
    sol = ''
    for lst in grid:
        lst_tmp = [str(x) for x in lst]
        sol += ' '.join(lst_tmp)
    print(sol)


def input_to_grid(grid_tmp):
    grid_tmp = grid_tmp.split(' ')
    grid_tmp = [int(x) for x in grid_tmp]
    grid = []
    row = []
    for val in grid_tmp:
        if len(row) == 9:
            grid.append(row)
            row = []
        row.append(val)
    grid.append(row)
    if len(grid) != 9 or len(row) != 9:
        raise ValueError('len invalid !!')
    
    return grid


test_number = input()
test_number = int(test_number)

for _ in range(test_number):

    grid = input()
    grid = input_to_grid(grid)
    solve_sdk(grid, 0, 0)

    print_grid(grid)
def is_valid_sudoku(sudoku):
    # Check column
    for i in range(9):
        column = []
        for j in range(9):
            if sudoku[j][i] in column:
                return False
            column.append(sudoku[j][i])
    
    # Check grid by grid 3x3
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            grid = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if sudoku[k+i][l+j] in grid:
                        return False
                    grid.append(sudoku[k+i][l+j])
    return True


sudoku = []
is_valid = True
for i in range(9):    
    line = []
    for j in input().split():
        n = int(j)
        
        if n in line:
            is_valid = False
        
        line.append(n)
    sudoku.append(line)


if is_valid:
    is_valid = is_valid_sudoku(sudoku)


print(str(is_valid).lower())
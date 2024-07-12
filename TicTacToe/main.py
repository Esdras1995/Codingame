def winner(line):
    return line.count('O') == 2 and "." in line

grid = []
win = False
sols = ['', '', '', '', '']
for i in range(3):
    line = input()
    
    if winner(line):
        line = line.replace('.', 'O')
        win = True
    
    grid.append(line)
    
    if not win:
        sols[0] += line[0]
        sols[1] += line[1]
        sols[2] += line[2]
        sols[3] += line[i]
        sols[4] += line[2-i]

if not win:
    for i in range(len(sols)):
        if win := winner(sols[i]):
            j = sols[i].index('.')
            i = j if i == 3 else i
            i = 2-j if i == 4 else i
            grid[j] = grid[j][:i] + 'O' + grid[j][i+1:]
            break


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print('\n'.join(grid) if win else 'false')
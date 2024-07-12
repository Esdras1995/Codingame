rows = int(input())
grid = []
for i in range(rows):
    row = input()
    grid.append(row)
message = input()

r = ''
for m in message:
    for i in range(len(grid)):
        if m in grid[i]:
            j = grid[i].split().index(m)
        else:
            continue
        
        if j != -1:
            r += str(i)+str(j)

print(r)
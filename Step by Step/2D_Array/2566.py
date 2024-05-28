grid = []
max_num = 0
row, col = 0, 0

for i in range(9):
    grid.append(list(map(int, input().split())))

for x in range(9):
    for y in range(9):
        if max_num <= grid[x][y]:
            row = x+1
            col = y+1
            max_num = grid[x][y]

print(max_num)
print(row, col)
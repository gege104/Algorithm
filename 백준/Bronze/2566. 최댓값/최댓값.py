matrix = []

for i in range(9):
    matrix.append(list(map(int, input().split())))

max_element = -1
max_x, max_y = 0, 0

for x in range(9):
    for y in range(len(matrix[x])):
        if matrix[x][y] > max_element:
            max_element = matrix[x][y]
            max_x, max_y = x+1, y+1

print(max_element)
print(max_x, max_y)

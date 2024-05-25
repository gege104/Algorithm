n, m = map(int, input().split())
matrix_1 = []
matrix_2 = []

for x in range(n):
    matrix_1.append(list(map(int, input().split())))

for y in range(n):
    matrix_2.append(list(map(int, input().split())))

for row in range(n):
    for col in range(m):
        print(matrix_1[row][col] + matrix_2[row][col], end=' ')
    print()
N, M = map(int, input().split())
matrix_1 = []
matrix_2 = []

for i in range(N*2):
    if i<N:
        matrix_1_element = list(map(int, input().split()))
        matrix_1.append(matrix_1_element)
    else:
        matrix_2_element = list(map(int, input().split()))
        matrix_2.append(matrix_2_element)

for j in range(N):
    matrix_sum = [x+y for x, y in zip(matrix_1[j], matrix_2[j])]
    print(*matrix_sum)

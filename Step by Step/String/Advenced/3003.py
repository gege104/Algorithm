chess = [1, 1, 2, 2, 2, 8]

n = list(input().split())
result = []

for i in range(len(chess)):
    result.append(chess[i]-int(n[i]))

for j in result:
    print(j, end=' ')
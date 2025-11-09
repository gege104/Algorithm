paper = [[-1]*100 for _ in range(100)]
N = int(input())

for i in range(N):
    left, bottom = map(int, input().split())
    right = left + 10
    top = bottom + 10
    
    for j in range(left, right):
        for k in range(bottom, top):
            paper[j][k] += 1

region = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] != -1:
            region += 1

print(region)
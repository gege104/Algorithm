N, M = map(int, input().split())
basket = [n for n in range(1, N+1)]

for x in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = list(reversed(basket[i-1:j]))
    
print(*basket)
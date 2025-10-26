N, M = map(int, input().split())
basket = [0 for x in range(N)]

for i in range(M):
    i, j, k = map(int, input().split())
    basket[i-1:j] = [k] * (j-i+1)

print(*basket)  # 언패킹 연산자로 리스트 형태가 아닌 원소 출력

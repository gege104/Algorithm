N, M = map(int, input().split())
basket = [(x+1) for x in range(N)]

for i in range(M):
    i, j = map(int, input().split())
    temp = basket[j-1]
    basket[j-1] = basket[i-1]
    basket[i-1] = temp

print(*basket)  # 언패킹 연산자로 리스트 형태가 아닌 원소 출력

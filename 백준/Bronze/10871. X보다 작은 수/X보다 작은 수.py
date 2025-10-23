N, X = map(int, input().split())
input_list = list(map(int, input().split()))

for i in range(N):
    if input_list[i] < X:
        print(input_list[i], end=" ")
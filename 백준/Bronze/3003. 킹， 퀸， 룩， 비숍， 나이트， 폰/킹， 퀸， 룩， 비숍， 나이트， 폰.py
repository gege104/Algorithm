chess = [1, 1, 2, 2 ,2, 8]
chess_input = list(map(int, input().split()))

result = [chess[i]-chess_input[i] for i in range(len(chess))]

print(*result)
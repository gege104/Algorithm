n = int(input())
cache = input()
result = 0

for i in range(n):
    result += int(cache[i])

print(result)
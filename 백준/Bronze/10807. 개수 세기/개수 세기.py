N = int(input())
input_list = input().split()
v = int(input())
count = 0

for i in range(N):
    if int(input_list[i]) == v:
        count += 1

print(count)
A, B = map(int, input().split())
C = int(input()) 

A *= 60
time = A + B + C

hour = time // 60
minute = time % 60

hour = hour % 24

print(hour, minute)

n = int(input())

for i in range(2*n):
    if i<n:
        print(' ' * (n-i-1), end='')
        print('*' * (2*i+1))
    else:
        print(' ' * (i-n+1), end='')
        print('*' * (2*(2*n-i)-3))
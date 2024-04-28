n = int(input())

for i in range(n):
    s = input()

    # len 말고 -1로 처리했으면 더 좋았을 것 같다.
    print(s[0]+s[len(s)-1])
word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for idx, code in enumerate(dial):
    idx += 3
    for w in word:
        if w in code:
            result += idx
            
print(result)
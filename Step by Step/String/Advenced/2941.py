croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in croatia_alphabet:
    s = s.replace(i, '*')

print(len(s))
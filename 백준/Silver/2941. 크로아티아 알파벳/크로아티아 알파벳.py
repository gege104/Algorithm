word = input()
alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for a in alphabet:
    word = word.replace(a, "*")

print(len(word))
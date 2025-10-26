students = [(x+1) for x in range(30)]

for i in range(28):
    n = int(input())
    students.remove(n)

print(min(students))
print(max(students))
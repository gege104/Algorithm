N = int(input())
group_word_num = 0

for i in range(N):
    word = input()
    unique_alphabet = set(word)
    dedupe_word = ""
    
    for j in range(len(word)):
        if j == len(word)-1:
            dedupe_word += word[j]
            break
        elif word[j] != word[j+1]:
            dedupe_word += word[j]
    
    if len(unique_alphabet) == len(dedupe_word):
        group_word_num += 1

print(group_word_num)
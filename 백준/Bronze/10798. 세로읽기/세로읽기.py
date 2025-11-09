word_list = []
word_max_len = 0
result_word = ""

for i in range(5):
    input_word = input()
    word_list.append(input_word)

    if len(input_word) > word_max_len:
        word_max_len = len(input_word)

# 단어 길이를 맞추기 위해 짧은 단어에 언더바 추가
new_word_list = [word+"_"*(word_max_len - len(word)) for word in word_list]

for i in range(word_max_len):
    for j in range(5):
        result_word += new_word_list[j][i]

result_word = result_word.replace("_", "")
print(result_word)
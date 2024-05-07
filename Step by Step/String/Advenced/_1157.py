# 틀린 문제

s = input().upper()
unique_s = list(set(s)) # 중복 제거

cnt_list = []

for x in unique_s:
    cnt = s.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_s[max_index])
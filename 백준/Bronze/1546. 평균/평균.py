N = int(input())
score_list = list(map(int, input().split()))

M = max(score_list)
new_score_list = [x/M*100 for x in score_list]

print(sum(new_score_list)/N)
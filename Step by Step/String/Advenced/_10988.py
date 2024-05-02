# 틀린 문제

s = input()

# collection[start:stop:step]
# start : 슬라이싱 작업이 시작되어야 하는 위치
# stop : 작업이 중지되어야 하는 위치
# step : 요소를 반복하는 순서

# 값을 뒤집어 보았을 때, 뒤집지 않은 원래의 값과 일치하는지를 확인
if s[::1] == s[::-1]:
    print(1)
else:
    print(0)
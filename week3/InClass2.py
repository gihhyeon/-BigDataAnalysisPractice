# [2] while 예제
# 1~50 사이의 숫자 중 정답 맞추기

import random

sol = random.randint(1,50)  # 정답

tries = 0   # 도전 횟수
userAnswer = 0

while userAnswer != sol:
    userAnswer = int(input("1~50 사이의 정답을 맞춰보세요>> "))
    tries += 1  # 도전 횟수 증가

    if (userAnswer == sol): # 정답을 맞춘 경우
        print("%d번 만에 맞췄습니다!" %tries)
        break
    elif userAnswer < sol:  # 정답보다 작은 숫자를 입력한 경우
        print("UP")
    elif userAnswer > sol:  # 정답보다 큰 숫자를 입력한 경우
        print("DOWN")
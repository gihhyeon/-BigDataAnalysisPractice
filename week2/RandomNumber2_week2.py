# 1~99까지 숫자 중 임의의 수를 발생시켜 덧셈 문제 10개 출제하여
# 정답률, 오답률 계산하기

import time
import random

correctCnt, wrongCnt = 0, 0

for i in range(1, 11):  # 1~10까지 반복
    x = random.randint(1,99)
    y = random.randint(1,99)

    #문제 출제----------------------------
    print(f"{i}번>> {x} + {y} = ")
    # 시간 측정 시작----------------------
    startTime = time.time()
    answer = int(input())
    endTime = time.time()
    # 시간 측정 종료------------------

    print("%.1f초 만에 답을 했네요" %(endTime-startTime))
    if answer == x + y:
        print("정답입니다")
        correctCnt += 1
    else:
        print("오답입니다")
        wrongCnt += 1

print("당신의 정답률 = %.1f%%" %(correctCnt/(correctCnt+wrongCnt)*100))
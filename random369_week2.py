# random.randrange(5) -> 0,1,2,3,4 중 하나
# random.randint(1,5) -> 1,2,3,4,5 중 하나

import random

n = random.randint(1, 99)
print("오늘의 숫자는 %d\n" %n)
num10 = n//10   # 10의 자리수
num1 = n % 10   # 1의 자리수

if num10 == 0:
    num10 = 2  # 3, 6, 9가 아닌 의미 없는 정수로 대체
if num1 == 0:
    num1 = 2   # 3, 6, 9가 아닌 의미 없는 정수로 대체

#박수 없음 / 박수 짝! / 박수 짝!짝! 조건 비교
if num10 % 3 == 0 and num1 % 3 == 0:
    print("박수 짝!짝!")
elif (num10 % 3 == 0 and num1 % 3 != 0) or (num10 % 3 != 0 and num1 % 3 == 0):
    print ("박수 짝!")
else:
    print("박수 없음")

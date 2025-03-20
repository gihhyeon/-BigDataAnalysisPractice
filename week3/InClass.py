# for : 반복횟수 알 경우 -> for i in range(10):
# while : 조건이 참인 경우 -> while 조건식:

# 소수 : 1과 자기 자신으로만 나뉘어지는 수
# [1] 3~100까지 소수를 모두 출력, 몇 개가 존재하는지 그 개수 출력

primeCnt = 0    # 소수의 개수
for n in range(3, 101):
    sosu = True # 소수라고 가정, 나머지가 0이 되면 False로 변경
    
    for i in range(2, n):   # 제수(나누는 수) : 2 ~ n-1까지 나눠야 됨
        if n % i != 0:
            continue
        else:
            sosu = False
            break

    if sosu == True:
        primeCnt += 1
        print("%5d" %n, end="")
    
print("\n3~100까지 소수의 개수 = %d개" %primeCnt)

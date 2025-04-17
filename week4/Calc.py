# 두 정수와 연산자 입력받아 사칙연산하는 함수 calc(num1, num2, op)를 작성하시오.

def calc(num1, num2, op):
    result = 0
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else:
        result = "잘못된 연산 기호입니다"
    return result

n1 = int(input("첫 번째 정수 입력>> "))
n2 = int(input("두 번째 정수 입력>> "))
op = input("연산자 입력(+,-,*,/)>> ")

print("%d %s %d = %s" %(n1, op, n2, calc(n1, n2, op)))
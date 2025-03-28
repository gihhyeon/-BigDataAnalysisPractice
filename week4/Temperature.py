# [함수 활용 1] 온도 변환 프로그램

def menu():
    print("1. 섭씨 -> 화씨")
    print("2. 화씨 -> 섭씨")
    print("3. 종료")
    user = int(input("메뉴를 선택하세요>> "))
    return user

def inputC():
    c = float(input("섭씨 온도 입력: "))
    return c

def inputF():
    f = float(input("화씨 온도 입력: "))
    return f

def ctof(temp):
    ftemp = (temp) * 9.0 / 5 + 32
    return ftemp

def ftoc(temp):
    ctemp = (temp - 32) * 5.0 / 9
    return ctemp

def main():
    while True:
        sel = menu()    # sel = 1, 2, 3 메뉴 선택
        if sel == 1:    # C -> F
            temp = inputC() # 섭씨온도 입력
            tt = ctof(temp) # 섭씨를 화씨로 변환
            print("섭씨 %.1f도 -> 화씨 %.1f도" %(temp, tt))
        elif sel == 2:  # F -> C
            temp = inputF() # 화씨 온도 입력
            tt = ftoc(temp) # 화씨를 섭씨로 변환
            print("화씨 %.1f도 -> 섭씨 %.1f도" %(temp, tt))

        elif sel == 3:
            print("온도변환 프로그램을 종료합니다.")
            break
        else:
            print("1~3 사이의 메뉴를 선택해야 됩니다.")
            continue


main()  # 시작
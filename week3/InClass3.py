# 친구 관리 프로그램
# [1] 친구 등록 [2] 친구 삭제 [3] 친구 이름 변경 [4] 친구 명단 출력 [5] 종료
# EX-----------------------
# 메뉴 선택>> 2
# 삭제할 친구의 이름 입력>> 홍길동
# 홍길동이라는 친구는 없습니다.
# [1] 친구 등록 [2] 친구 삭제 [3] 친구 이름 변경 [4] 친구 명단 출력 [5] 종료
# 메뉴 선택>> 5 (종료 누를 때까지 계속 반복)

def PrintMenu():
    print('-'*25)
    print("[1] 친구 등록 [2] 친구 삭제 [3] 친구 이름 변경 [4] 친구 명단 출력 [5] 종료")
    print('-'*25)


friend = [] # 공백 리스트 생성
menu = 0

while menu != 5:
    PrintMenu()     # 함수 호출
    menu = int(input("메뉴 선택>> "))

    if menu == 1:   # 친구 등록
        name = input("새로운 친구의 이름 입력>> ")
        friend.append(name)

    elif menu == 2: # 친구 삭제
        delName = input("삭제할 친구의 이름 입력>> ")
        if delName in friend:
            friend.remove(delName)  # 값으로 삭제 -> .remove(값)
            print("삭제 성공")
        
    elif menu == 3: # 친구 이름 변경
        oldName = input("변경할 친구의 이름 입력>> ")
        if oldName in friend:
            no = friend.index(oldName)
            newName = input("새로운 이름 입력>> ")
            friend[no] = newName
            print("수정 완료")

    elif menu == 4: # 친구 명단 출력
        if len(friend) > 0: # 등록된 친구가 1명 이상이라면
            print(friend)
        else:
            print("친구 목록이 비어있습니다")

    elif menu == 5: # 종료
        break
    else:
        print("잘못된 입력입니다")
        menu = 0

print("프로그램 종료...")
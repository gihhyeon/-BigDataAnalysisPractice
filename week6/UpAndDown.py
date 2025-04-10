import random
from tkinter import *

# 1 ~ 100 사이의 숫자 중 정답 설정
answer = random.randint(1, 100)
# random.randrange(100) : 0 ~ 99까지
# random.choice(리스트) : 리스트의 여러 값 중 하나를 선택

cnt = 0         # 도전 횟수
def TryFunc():  # [도전] 버튼을 눌렀을 때 동작할 함수
    global cnt
    user = int(userEntry.get()) # 엔트리의 값을 가져와 정수형으로 바꿈
    cnt += 1    # 도전 횟수 증가
    if user == answer:
        msg = "정답! " + str(cnt) + "번 만에 성공!"
    elif user < answer: # 작은 숫자를 입력한 경우
        msg = "UP! " + str(user) + "보다 큰 수를 입력해야 함"
    else:
        msg = "Down! " + str(user) + "보다 작은 수를 입력해야 함"

    # 출력할 결과 메세지
    resultLabel["text"] = msg
    # 엔트리 값 지우기
    userEntry.delete(0, 3)

def ResetFunc():    # [초기화] 버튼을 눌렀을 때 동작할 함수
    # 도전 횟수 초기화

    # 정답 초기화(재설정)

    resultLabel["text"] = "초기화 되었으므로 다시 도전하세요"

window = Tk()
window.geometry("650x70")
window.title("Up And Down Game")

# 위젯 생성하여 부착하기
lbl = Label(window, text="숫자 맞추기 게임에 온 것을 환영합니다!", font="25")
lbl.pack()
userEntry = Entry(window)
userEntry.pack(side=LEFT)

# 버튼을 클릭했을 때 TryFunc 함수가 호출되도록
tryButton = Button(window, text="도전", fg="blue", command=TryFunc)
tryButton.pack(side=LEFT)

# 버튼을 클릭했을 때 ResetFunc 함수가 호출되도록
resetButton = Button(window, text="초기화", fg="red", command=ResetFunc)
resetButton.pack(side=LEFT)
resultLabel = Label(window, text="1~100 사이의 숫자를 입력하세요.")
resultLabel.pack(side=LEFT)


window.mainloop()

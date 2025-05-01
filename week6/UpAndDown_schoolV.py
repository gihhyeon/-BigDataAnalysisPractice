import random
from tkinter import *

# 1~100 사이의 숫자중 정답 설정
answer = random.randint(1,100)
# random.randrange(100) : 0~99까지
# random.choice(리스트) : 리스트의 여러 값 중 하나를 선택

cnt = 0             # 도전횟수
def Tryfunc():      # [도전]버튼을 눌렀을때 동작할 함수
    global cnt
    user = int(userEntry.get())     # 엔트리의 값을 가져와 정수형으로 바꿈
    cnt += 1        # 도전횟수 증가
    if user==answer:
        msg = "정답! "+str(cnt)+"번만에 성공!!!"
    elif user<answer:       # 작은 숫자를 입력한 경우
        msg = "UP!!! "+str(user)+"보다 큰 수를 입력해야 함"
    else:           # 큰 숫자를 입력한 경우
        msg = "Down~ "+str(user)+"보다 작은 수를 입력해야 함"

    # 출력할 결과 메세지
    resultLabel["text"] = msg
    # 엔트리 값 지우기
    userEntry.delete(0, 10)

def ResetFunc():    # [초기화]버튼을 눌렀을때 동작할 함수
    global cnt, answer
    # 도전 횟수 초기화
    cnt = 0
    # 정답 초기화(재설정)
    answer = random.randint(1, 100)

    resultLabel["text"] = "초기화되었으므로 다시 도전하세요~"
    userEntry.delete(0, END)

window = Tk()
window.geometry("500x70")
window.title("Up And Down Game")

# 위젯 생성하여 부착하기
lbl = Label(window, text="숫자 맞추기 게임에 온것을 환영합니다!!!", font="25")
lbl.pack()
userEntry = Entry(window)
userEntry.pack(side="left")

# 버튼을 클릭했을 때, Tryfunc함수가 호출되도록 명령내림----------------------------
tryButton = Button(window, text="도전", fg="Blue", command=Tryfunc)
tryButton.pack(side="left")
resetButton = Button(window, text="초기화", fg="red", command=ResetFunc)
resetButton.pack(side="left")
resultLabel = Label(window, text="1~100사이의 숫자를 입력하세요.")
resultLabel.pack(side="left")
window.mainloop()
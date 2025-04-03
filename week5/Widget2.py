# [1] 위젯과 배치관리자 연습2
from tkinter import *

window = Tk()
window.geometry("500x300")

# 함수 구현
def process():
    print("버튼이 클릭되었습니다.")
    print("이벤트 처리 프로그램")


# 위젯 만들기
l1 = Label(window, text="화씨", height=3)
l2 = Label(window, text="섭씨", height=3)
e1 = Entry(window)
e2 = Entry(window)
btn = Button(window, text = "화씨 -> 섭씨", height=3, command=process)

# 컨테이너에 위젯 부착하기
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
btn.grid(row=2, column=1)


window.mainloop()
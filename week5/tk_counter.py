from tkinter import *

window = Tk()

# 버튼이 클ㅣ 될 때다 1씩 증가하는 변수
cnt = 0

def clicked():
    global cnt
    cnt += 1
    l1["text"] = "버튼 클릭 횟수 : " + str(cnt)

def erased():   # 초기화 버튼을 누르면 cnt = 0, l1 위젯도 초기화
    global cnt
    cnt = 0
    l1["text"] = "초기화 되었습니다."


# 위젯 생성
l1 = Label(window, text=" ")
btn1 = Button(window, text="클릭", command=clicked)
btn2 = Button(window, text="초기화", command=erased)

#부착하기
l1.pack
btn1.pack
btn2.pack

window.mainloop()
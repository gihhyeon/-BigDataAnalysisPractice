# [1] 위젯과 배치 관리자 연습
from tkinter import *

window = Tk()   # 윈도우 창 생성

# 버튼들이 왼->오 부착될 컨테이너 프레임 생성
f = Frame(window)   # 윈도우 창에 보여질 프레임 생성

btn1 = Button(f, text="버튼#1", fg="black", bg="pink", width=20, height=3) # 버튼 생성
btn2 = Button(f, text="버튼#2", fg="yellow", bg="blue", width=20, height=3)
btn3 = Button(f, text="버튼#3", fg="red", bg="white", width=20, height=3)
btn4 = Button(f, text="버튼#4", fg="green", bg="orange", width=20, height=3)

btn1.pack(side="left")
btn2.pack(side="left")
btn3.pack(side="left")
btn4.pack(side="left")

# grid 배치
# btn1.grid(row=0, column=0)  # 0행 0열에 부착
# btn2.grid(row=0, column=1)  # 0행 1열에 부착
# btn3.grid(row=1, column=0)  # 1행 0열에 부착
# btn4.grid(row=1, column=1)  # 1행 1열에 부착

# place 배치 : x좌표 y좌표 지정
# btn1.place(x=0, y=10)
# btn2.place(x=40, y=60)
# btn3.place(x=80, y=110)
# btn4.place(x=120, y=160)

l1 = Label(window, text="이 레이블은 버튼 위에 배치됩니다.")
l1.pack()   # 제일 위에 부착
f.pack()    # 


window.mainloop()
# [활용 1] 온도 변환 프로그램

from tkinter import *

window = Tk()

# 함수 구현
# [섭씨로 변환] 함수 구현
def ToC():
    tf = float(e1.get())*5/9    
    tc = (tf-32.0)  # 섭씨로 계산
    e2.delete(0, END)
    e2.insert(0, str(tc))

# [화씨로 변환] 함수 구현
def ToF():
    tc = float(e2.get())
    tf = (tc*9.0/5) + 32.0  # 화씨로 계산
    e1.delete(0, END)
    e1.insert(0, str(tf))

# [확대] 함수 구현
def expand():   # imgL의 크기가 2배로 확대
    imgL["width"] = 300
    imgL["height"] = 300

# [축소] 함수 구현
def reduce():   # imgL의 크기가 1/2로 축소
    imgL["width"] = 100
    imgL["height"] = 100
                

# 위젯 생성
l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
e1 = Entry(window)
e2 = Entry(window)
btn1 = Button(window, text="섭씨로 변환", command=ToC)
btn2 = Button(window, text="화씨로 변환", command=ToF)
btn3 = Button(window, text="확대", command=expand)
btn4 = Button(window, text="축소", command=reduce)
p = PhotoImage(file="week5/lion-cheer_thumb_300.gif")
imgL = Label(image=p, width=200, height=200)

# 위젯 부착
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn4.grid(row=2, column=3)

imgL.grid(row=0, column=2, columnspan=4)

window.mainloop()
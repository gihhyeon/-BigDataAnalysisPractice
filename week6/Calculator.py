from tkinter import *

# (1) 윈도우 객체 생성
window = Tk()
window.title("계산기")

# (2) 엔트리 객체 생성 후, grid 배치관리자로 부착(5열 병합)
e = Entry(window, width=30, bg="gray", fg="black")
e.grid(row=0, column=0, columnspan=5)

# (3) 버튼 리스트 생성  %, //, **, . 4열에 4개의 버튼 추가
buttons = [
    "7", "8", "9", "+", "%",
    "4", "5", "6", "-", "//",
    "1", "2", "3", "*", "**",
    "0", "C", "=", "/", "."
]



# (4) 똑같은 크기를 갖는 버튼 생성하여 grid 배치관리자로 부착 - 이벤트 발생시 함수 연결
#     이벤트가 발생하면 클릭한 키의 값이 '=', 'C' 값과 같은지 비교하여 동작 구현
#     그 이외의 버튼이 눌리면 e에 삽입
# --> 1행 0열부터 3열까지 버튼 생성하여 부착
r = 1
c = 0

for char in buttons:

    def click(key = char):
        if key == "=":
            result = eval(e.get())
            e.delete(0, END)
            e.insert(0, str(result))
        elif key == "C":
            e.delete(0, END)
        else:
            e.insert(END, key)

    b = Button(window, text=char, width=6, height=3, command=click)
    b.grid(row=r, column=c)
    c = c + 1

    if c > 4:   # 한 줄에 5개씩
        r = r + 1
        c = 0

window.mainloop()
import random
from tkinter import *

window = Tk()
frame = Frame(window)
lbl = Label(window, text="아래 이미지 중 하나를 선택하세요", font=("Stencil", "20"))
lbl.pack()  # 제일 위쪽에 부

# 이미지를 읽어서 객체로 만든다.
rock_image = PhotoImage(file="/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/RSP_Img/rock.png")
paper_image = PhotoImage(file="/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/RSP_Img/paper.png")
scissors_image = PhotoImage(file="/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/RSP_Img/scissors.png")

# 사용자가 버튼을 누르면 호출되는 콜백 메소드
def pass_s():   # 가위 이미지를 클릭했을 때
    decide("가위")
def pass_r():   # 바위 이미지를 클릭했을 때
    decide("바위")
def pass_p():   # 보 이미지를 클릭했을 때
    decide("보")

# 이미지를 가지는 버튼 생성 -> 사람이 이미지 버튼을 클릭하면 호출할 함수 연결
rButton = Button(frame, image=rock_image, command=pass_r)
rButton.pack(side="left")
pButton = Button(frame, image=paper_image, command=pass_p)
pButton.pack(side="left")
sButton = Button(frame, image=scissors_image, command=pass_s)
sButton.pack(side="left")

frame.pack()    # 프레임을 윈도우에 부착

comLabel = Label(window, text="컴퓨터가 선택한 결과", font=("Stencil", "20"))
comLabel.pack()
comImage = Label(window, image=rock_image)    # 실행하면 기본 이미지(바위) 출력
comImage.pack()
resultLabel = Label(window, text="", font=("Stencil", "20"))
resultLabel.pack()

# (1) 컴퓨터가 가위, 바위, 보 중 하나를 선택
# (2) 컴퓨터의 선택에 따라 출력할 이미지 결정
# (3) 사람과 비교해서 승패 판단
# (4) 결과로 내보낼 메시지 결정

# 가위바위보 로직
def decide(human):
    computer = random.choice(["가위", "바위", "보"])
    if computer == "바위":
        comImage["image"] = rock_image
    elif computer == "보":
        comImage["image"] = paper_image
    else:
        comImage["image"] = scissors_image

    if (computer == "바위" and human == "보") or \
       (computer == "보" and human == "가위") or \
       (computer == "가위" and human == "바위"):
        result_text = "인간 승리!"
    elif computer == human:
        result_text = "비겼습니다."
    else:
        result_text = "컴퓨터 승리!"

    resultLabel["text"] = result_text


window.mainloop()
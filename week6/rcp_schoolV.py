import random
from tkinter import *

# 윈도우와 프레임 생성
window = Tk()
frame = Frame(window)
lbl = Label(window, text="아래 이미지중 하나를 클릭하세요", font=("Stencil", 20,"bold"))
lbl.pack()          # 제일 위쪽에 라벨 부착

# 가위 이미지, 바위 이미지, 보 이미지 갖는 변수 생성
s_img = PhotoImage(file="D://hja/src/RSP_Img/scissors.png")
r_img = PhotoImage(file="D://hja/src/RSP_Img/rock.png")
p_img = PhotoImage(file="D://hja/src/RSP_Img/paper.png")

# 함수 정의------------------------------------------------------------------------------
def pass_s():   # 가위 이미지를 클릭했을 때
    decide("가위")
def pass_r():   # 바위 이미지를 클릭했을 때
    decide("바위")
def pass_p():   # 보 이미지를 클릭했을 때
    decide("보")

def decide(human):      # 사람이 이미지버튼을 클릭
    # (1) 컴퓨터가 "가위","바위","보" 중 하나를 선택
    com = random.choice(["가위", "바위", "보"])
    # (2) 컴퓨터의 선택에 따라 라벨의 이미지 결정
    if com == "가위":
        comImage["image"] = s_img
    elif com == "바위":
        comImage["image"] = r_img
    else:
        comImage["image"] = p_img

    # (3) 사람과 비교
    if com==human:
        msg = "사람:"+human+"   컴퓨터:"+com+" => 무승부"
    elif (com=="가위" and human=="보") or(com=="바위" and human=="가위") or(com=="보" and human=="바위"):
        msg = "사람:"+human+"   컴퓨터:"+com+" => 컴퓨터 승리!"
    else:
        msg = "사람:"+human+"   컴퓨터:"+com+" => 사람 승리!"

    # (4) 결과로 출력할 메세지 결정
    resultLabel["text"] = msg

# 이미지를 갖는 버튼 생성 ==> 사람이 이미지버튼을 클릭하면 호출할 함수 연결
sButton = Button(frame, image=s_img, command=pass_s)
rButton = Button(frame, image=r_img, command=pass_r)
pButton = Button(frame, image=p_img, command=pass_p)
sButton.pack(side="left")
rButton.pack(side="left")
pButton.pack(side="left")
frame.pack()        # 프레임을 윈도우에 부착


comLabel = Label(window, text="컴퓨터가 선택한 결과", font=("Stencil", 20,"bold"))
comLabel.pack()
comImage = Label(window, image=r_img)       # 실행하면 기본이미지(바위) 출력
comImage.pack()

resultLabel = Label(window, text="", font=("Stencil", 20,"bold"))      # 결과 출력 라벨
resultLabel.pack()

window.mainloop()
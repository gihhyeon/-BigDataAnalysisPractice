'''
[리스트와 gif 이미지, 버튼 활용]
[이전] 버튼 [다음] 버튼과 리스트의 0번방의 이미지가 출력
[다음] 버튼 -> 인덱스 번호 0-1-2-3-4-5 다음 0으로 초기화
[이전] 버튼 -> 3번방의 이미지 3->2->1->0->5 로 설정
'''

from tkinter import *

#/Users/gihyeonkim/Downloads/
fname = ["d1.gif", "d2.gif", "d3.gif", "d4.gif", "d5.gif", "d6.gif"]

num = 0 # 초기 인덱스 번호 = 0

def funcNext(): # [다음] 버튼 눌렀을 때, 동작 함수
    global num
    num += 1    # 방 번호 증가

    if num > 5: # 6번째 이미지는 5번 방!
        num = 0 # 시험 나올 듯?
    # 인덱스 번호에 해당하는 이미지를 라벨에 출력
    photo = PhotoImage(file="/Users/gihyeonkim/Downloads/" + fname[num])
    pLabel["image"] = photo
    pLabel.image = photo

def funcPrevious(): # [이전] 버튼 눌렀을 때, 동작 함수
    global num
    num -= 1  # 인덱스 감소

    if num < 0:  # 0보다 작아지면 마지막 인덱스로
        num = 5

    photo = PhotoImage(file="/Users/gihyeonkim/Downloads/" + fname[num])
    pLabel["image"] = photo
    pLabel.image = photo

window = Tk()
window.geometry("600x600")
window.title("사진 앨범 프로그램")

# [이전] [다음] 버튼 생성하여 부착      여기 시험 나옴!!
prevBtn = Button(window, text="이전", width=6, command=funcPrevious)
nextBtn = Button(window, text="다음", width=6, command=funcNext)
prevBtn.place(x=200, y=30)
nextBtn.place(x=320, y=30)


# 이미지 갖는 라벨 생성하여 부착 -> 실행했을 때 0번 방의 이미지 출력
photo = PhotoImage(file="/Users/gihyeonkim/Downloads/" + fname[0])
pLabel = Label(window, image=photo)
pLabel.place(x=100, y=80)

window.mainloop()
# [1] 파일 열기
inF = open("/Users/gihyeonkim/Downloads/test.txt", "r")
outF = open("/Users/gihyeonkim/Downloads/result.txt", "w")

# [2] 파일 처리 -> 한 줄씩 출력
inStr = inF.readline()  # 첫 번째 줄
print(inStr, end="")
inStr = inF.readline()  # 두 번째 줄
print(inStr, end="")
inStr = inF.readline()  # 세 번째 줄
print(inStr, end="")

# 총점, 평균, 수강자 수
sum = 0
n = 0
jumsu = inF.readline()  # 네 번째 줄 읽어오기
while jumsu != "":
    sum += int(jumsu)   # 총점에 누적
    n += 1              # 학생수 증가
    jumsu = inF.readline()

outF.write("총점 = " + str(sum) + "점" + "\n")
outF.write("평균 점수 = " + str(sum/n) + "점" + "\n")
inF.close()
outF.write("수강자 수 = " + str(n) + "명")

# [3] 파일 닫기
inF.close()
outF.close()
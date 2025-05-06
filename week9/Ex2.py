def showList(hList):
    for data in hList:
        print(data, end="\t")
    print()

with (open("/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/수업자료/파이썬 Beginner 소스/CSV/singer1.csv", "r", encoding='cp949') as inFp):  # 별명
    with open("/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/-BigDataAnalysisPractice/new_singer.csv", "w") as outFp:
        header = inFp.readline()    # 첫 번째 줄 읽어오기
        header = header.strip()     # 열 이름 앞뒤의 공백 제거
        headerList = header.split(",")
        # showList(headerList)      # 콘솔에 출력

        headerStr = ",".join(map(str, headerList))
        outFp.write(headerStr + "\n")

        for data in inFp:
            inStr = data.strip()
            row = inStr.split(",")
            # showList(row)
            # 마지막 열의 데뷔년도에서 '.'을 '/'로 교체
            row[-1] = row[-1].replace('.', '/')
            # 끝에서 두번째 열(평균키) 소수점 첫째 자리까지
            cm = "{0:.1f}".format(int(row[-2])) # 수치 데이터로 형변환 후 소수점 첫째 자리까지 지정
            row[-2] = cm
            rowStr = ",".join(map(str, row))
            outFp.write(rowStr + "\n")

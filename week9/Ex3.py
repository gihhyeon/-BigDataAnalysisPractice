def showList(hList):
    for data in hList:
        print(data, end="\t")
    print()

with (open("/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/수업자료/파이썬 Beginner 소스/CSV/singer1.csv", "r", encoding='cp949') as inFp):  # 별명
    with open("/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/-BigDataAnalysisPractice/singerOver165.csv", "w") as outFp:
        header = inFp.readline()    # 첫 번째 줄 읽어오기
        header = header.strip()     # 열 이름 앞뒤의 공백 제거
        headerList = header.split(",")
        # showList(headerList)      # 콘솔에 출력

        # 평균 키의 열 번호 알아내기
        cmNo = headerList.index("평균 키")
        # 데뷔 일자의 열 번호 알아내기
        yearNo = headerList.index("데뷔 일자")

        #출력할 열 제목만 재구성
        headerList = [headerList[0], headerList[1], headerList[cmNo], headerList[yearNo]]

        headerStr = ",".join(map(str, headerList))
        outFp.write(headerStr + "\n")

        for data in inFp:
            inStr = data.strip()
            row = inStr.split(",")
            # showList(row)

            # 평균 키가 165 이상인 데이터 추출
            if int(row[cmNo]) >= 165:
                # 출력할 열 데이터 재구성
                rowList = [row[0], row[1], row[cmNo], row[yearNo]]
                rowStr = ",".join(map(str, rowList))
                outFp.write(rowStr + "\n")

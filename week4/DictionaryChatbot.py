# 프로그래밍 언어 개발 연도 안내 챗봇

query = input("프로그래밍 언어 입력 : ")
query = query.lower()   # 소문자로

if "c" in query:
    print("C언어는 1972년에 태어났어요.");
elif "java" in query:
    print("Java는 1995년에 태어났어요.");
elif "python" in query:
    print("Python은 1991년에 태어났어요.");
else:
    print("등록되지 않은 언어입니다.")

dic = {'c':1972,
       'java':1995,
       'python':1991,
       'go':2009,
       'pascal':1969}

query = input("프로그래밍 언어 입력 : ")
k = query.lower()

if k in dic:
    year = dic.get(k)
    print("{}언어는 {}년에 태어났어요".format(query, year))
else:
    print("등륵되지 않은 언어입니다.")
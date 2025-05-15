import pandas as pd

data = { "이름" : ["이순신", "황희", "유관순", "김유신"],
         "나이" : [33, 27, 20, 22],
         "생년월일" : ["1993-01-31", "1999-12-12", "2006-03-01", "2004-08-15"]}

# 데이터 프레임 생성
df = pd.DataFrame(data)
print(df)

# 기본인덱스 0, 1, 2, 3을 변경하기
indexList = ["가", "나", "다", "라"]
df2 = pd.DataFrame(data, index=indexList)
print(df2)

# 모든 인덱스 정보, 모든 열 이름 출력
print(df2.index)
print(df2.columns)

# "이름" 열 추출
name = df2["이름"]
print(name)
print(type(name))
age = df2["나이"]
print(age)
print(type(age))

# "나이" 열 이름을 "연령"으로 변경
age.name = "연령"
print(age)

# 인덱스가 "다"인 행 추출
daRow = df2.loc["다"]    # daRow = df2.iloc[2]
print(daRow)
print(type(daRow))

# "다" 행 "생년월일" 열 추출
print(df2.loc["다"]["생년월일"])
print(df2.iloc[2,2])

# 기본적으로 끝에 열 추가가 됨(방법 1)
df2["몸무게"] = [77.2, 65.4, 42.9, 73.5]
print(df2)

# 열 추가(방법 2) : 데이터 중 일부분의 값을 모르는 경우
grade = pd.Series([2, 3], index=["다", "라"])
df2["학년"] = grade   # '가', '나' 인덱스 행의 학년: NaN 대체 , Null : NaN(Not a Number)
print(df2)

tel = pd.Series(["010-4444-4444", "010-1111-1111"], index=["라", "가"])
df2["연락처"] = tel
print(df2)

# 열 추가(방법 3) : 특정 위치에 삽입
df2.insert(2, "취미", ["피아노", "골프", "수영", "영화 보기"])
print(df2)

# 행 추가(방법 1) : 기본적으로 마지막 행에 추가됨
df2.loc["카"] = ["정약용", 22, "과학 실험", "2005-05-05", 64.0, 3, "010-9999-8888"]
print(df2)

# 행 추가(방법 2) : 여러 개의 행 삽입하려면 -> 데이터 프레임 생성 후 -> 2개의 데이터 프레임 결합
grp = {"이름":["제니", "로제", "지수"],
       "나이":[23, 22, 21],
       "몸무게":[48.2, 45.4, 50.7]}

grp_df = pd.DataFrame(grp, index=['블핑', '블핑', '블핑'])
df2 = pd.concat([df2, grp_df])
print(df2)

# 1개 열 삭제
df2 = df2.drop(["연락처"], axis=1) # 열 방향에서 "연락처" 열 찾아 제거
# 1개 행 삭제
df2 = df2.drop(["라"], axis=0)   # axis=0 속성 생략 가능 -> 행에서 제거
print(df2)

# 여러 개 열 삭제
df2 = df2.drop(["생년월일", "학년"], axis=1)
# 여러 개 행 삭제
df2 = df2.drop(["다", "블핑"]) # 행에서 제거 : 총 4개 행 제거
print(df2)

df2.loc["파"] = {"이름":"김구", "나이":25}
print(df2)

# 수치 데이터가 있는 행의 개수, 평균, 표준편차, 최대값, 25% 50% 75% 등 정보 기술
print(df2.describe())
print(df2.mean(numeric_only=True))
print(df2.count(numeric_only=True))
print(df2["이름"].count())


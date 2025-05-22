import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/수업자료/"
raw_df = pd.read_csv(path + "owid-covid-data.csv")

selCol = ["iso_code", "location", "date", "total_cases", "population"]
df = raw_df[selCol]

kor_df = df[df.location == "South Korea"]
kor_date_index_df = kor_df.set_index("date")
usa_df = df[df.location == "United States"]
usa_date_index_df = usa_df.set_index("date")

# 그래프의 x축: 날짜, y축: 대한민국 확진자 수, 미국 확진자 수
kor_total_case = kor_date_index_df["total_cases"]   # 결과는 시리즈로 반환
usa_total_case = usa_date_index_df["total_cases"]

print(kor_total_case.head(10))
print(usa_total_case.head(10))

# 그래프로 시각화하려면? 데이터 프레임 필요!
# index = kor_date_index_df.index ----> x축

# 결과 >> 미국 그래프가 한국 그래프보다 훨씬 위에 출력됨
# 미국 코로나 상황이 더 안 좋다라고 해석하기 어려움 -> 인구 차이 때문에
# 인구 대비 확진자 비율을 구해야 함 -> population 열의 아무 행의 인구 가져오기
kor_population = kor_date_index_df["population"]["2020-03-20"]
usa_population = usa_date_index_df["population"]["2020-03-20"]

print("미국 인구: ", usa_population, ", 한국 인구: ", kor_population)
rate = round(usa_population/kor_population, 2)
final_df = pd.DataFrame( {
    "KOR" : kor_total_case * rate,
    "USA" : usa_total_case }, index = kor_date_index_df.index
)   # 딕셔너리의 키 : 그래프에서 범례로, 딕셔너리의 값 : 그래프로 출력
final_df.plot.line()

# 2022년도부터 그래프로 시각화하려면? -> 슬라이싱
final_df["2022-01-01" : ].plot.line(rot=30)
plt.show()

raw_hawaii_df = pd.read_csv(path + "hawaii-covid-data.csv")
print(raw_hawaii_df.info())

# 날짜, 확진자 수 추출
filter_hawaii_df = raw_hawaii_df[["submission_date", "tot_cases"]]
print(filter_hawaii_df.head(10))

# 뒤죽박죽인 날짜를 오름차순 정렬 : 데이터프레임.sort_values(by="정렬 열")
sorted_hawaii_df = filter_hawaii_df.sort_values(by="submission_date")
print(sorted_hawaii_df.head(10))

# '년-월-일' 날짜 타입을 갖는 'date' 열을 끝에 추가
sorted_hawaii_df['date'] = pd.to_datetime(filter_hawaii_df['submission_date'])
print(sorted_hawaii_df.head(10))

# 날짜(date) 열을 기준으로 오름차순 정렬
# 기능을 수행하면 새로운 변수를 생성하지 말고, 원본 객체의 값에 반영되도록!
# inplace = True 속성 적용
sorted_hawaii_df.sort_values(by="date", inplace=True)
print(sorted_hawaii_df.head(10))

# 하와이 총 인구수를 구글링하여 변수에 저장
hawaii_population = 1_447_154    # 파이썬에선 천 단위 구분 기호 ,를 _로 대체함
hawaii_rate = round(hawaii_population/kor_population, 2)
print(hawaii_rate)

# 하와이 확진자 수로 이뤄진 시리즈 생성
hawaii_total_case = sorted_hawaii_df['tot_cases']
print(hawaii_total_case.head(10))
print(str(kor_total_case.index.dtype))
print(str(hawaii_total_case.index.dtype))

# 대한민국 인덱스(date) 타입인 'string'으로 변경하여 통일시키기
# 원본.index.astype("string")
hawaii_total_case.index = hawaii_total_case.index.astype('string')

# 확진자 비율(hawaii_rate:0.03)을 적용한 최종 데이터 프레임(KOR, HAWAII) 생성
final_hawaii_df = pd.DataFrame( {
    "KOR" : kor_total_case * rate,
    "HAWAII" : hawaii_total_case }, index = kor_date_index_df.index
)
final_df.plot.line()

final_df["2022-01-01" : ].plot.line(rot=30)
plt.show()

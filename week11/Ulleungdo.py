import pandas as pd

from week9.Ex3 import yearNo

path = "/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/수업자료/"
wdf = pd.read_csv(path + "weather2.csv").set_index("일시")

# 새로운 열 'year' 만들기
wdf['year'] = pd.DatetimeIndex(wdf.index).year
print(wdf)

# 'year' 열을 그룹화하고, 평균 값 구하기
year_means = wdf.groupby("year").mean(numeric_only=True)
print(year_means)

# 불완전한 행(2010, 2020) 삭제 .drop()
year_means = year_means.drop([2010, 2020])
print(year_means)
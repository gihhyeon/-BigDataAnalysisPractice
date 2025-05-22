import matplotlib.pyplot as plt
import pandas as pd

'''
data = [173, 165, 168, 177, 161]

plt.plot(data)  # 기본 그래프 : 선 그래프
plt.ylabel("Cm")
plt.title("2025 Cm of Student")
plt.show()      # 그래프 창 보이게
'''



path = "/Users/gihyeonkim/Desktop/school/2025_1/빅데이터분석실습/수업자료/"
wdf = pd.read_csv(path + "weather2.csv").set_index("일시")

# 새로운 'month' 열 만들기
wdf["month"] = pd.DatetimeIndex(wdf.index).month
month_means = wdf.groupby("month").mean(numeric_only=True)

# 막대 그래프
month_means["평균 기온"].plot(kind="bar", label = "월 평균 기온")
plt.legend()
plt.show()
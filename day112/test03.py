"""
문제
월 입력 >> 12
일 입력 >> 11

a.csv 에 존재 하는
12월 11일 최고 기온 데이터 들과
최저 기온 데이터들을 한번에 show() 해주세요 !
단, 범례를 maxTemp / minTemp 하고,
빨간색 / 파란색 그래프로 표기 하세요.
"""

import matplotlib.pyplot as plt
import csv

month = input('월 입력 >> ')
date = input('일 입력 >> ')

maxTempList = []
minTempList = []
tempYear = []

with open('a.csv', 'r', encoding='cp949') as file:  # 윈도우 인코딩은 cp949 이다.
    data = csv.reader(file)
    header = next(data)
    print(header)

    for row in data:
        if row[-1] == '':  # -1은 맨 마지막 데이터 (reverse 느낌)  / 최고 기온 구하기
            continue
        if row[3] == '':  # 최저 기온 구하기
            continue
        if row[0].split('-')[1] == month and row[0].split('-')[2] == date:  # 0번째 열의 행에서 -을 기준으로 인덱스로 구분 해서 입력 값과 비교
            tempYear.append(float(row[0].split('-')[0]))
            maxTempList.append(float(row[-1]))
            minTempList.append(float(row[3]))

plt.title('TEMPLIST' + month + 'MONTH' + date + 'DATE')
plt.plot(tempYear, maxTempList, color='red', label='maxTempList')  # 첫번째 인자 == x축
plt.plot(tempYear, minTempList, color='blue', label='minTempList')  # 두번째 인자 == y축
plt.legend()
plt.show()

import matplotlib.pyplot as plt
import csv  # csv 파일 불러 오기

maxTempList = []

with open('a.csv', 'r') as file:
    data = csv.reader(file)
    header = next(data)
    print(header)

    for row in data:
        if row[-1] == '':  # 처음 row 가 없으면 (데이터가 없으면 스킵 ~)
            continue
        if row[0].split('-')[1] == '08' and row[0].split('-')[2] == '08':  # 내가 보는 데이터의 0번째 row (날짜) 의 값이 8월 이라면 ~
            maxTempList.append(float(row[-1]))
            # 8월 이라는 조건을 붙혀줌으로써, 데이터 출력의 양이 확연 하게 줄어든 것을 알 수 있다.
            # 3만개 가량의 데이터에서 3천개 가량의 데이터로 10 분에 1로 줄었다.

print(len(maxTempList))

plt.title('maxTempList')  # 제목
plt.plot(maxTempList, color='red', label='maxTempList')
plt.legend()
plt.show()

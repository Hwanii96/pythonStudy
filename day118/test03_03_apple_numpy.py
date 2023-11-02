import csv
import matplotlib.pyplot as plt
import numpy as np

# pyplot 과 numpy 를 같이 사용 해서, 효율적으로 데이터를 시각화 !

with open('apple.csv', 'r') as file:
    data = csv.reader(file)
    header = next(data)
    print(header)
    print()

    area = input('출력할 지역 입력 >> ')
    for row in data:
        if area in row[0]:
            sample = np.array(row[3:], dtype=str)
            # dtype = int 로 하려면, 액셀 파일에 , 를 모두 지워야 한다.

print(sample)

plt.plot(sample)
plt.show()

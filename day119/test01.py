import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rc  # 폰트 설정을 위한 모듈 추가.
import numpy as np

with open('korea.csv', 'r') as file:
    data = csv.reader(file)  # csv 모듈의 reader() 함수를 사용 해서, data 변수를 행을 나타내는 이터레이터로 만들기.
    header = next(data)  # 첫번째 행을 데이터를 읽고, header 변수에 담아서, print() 하기.
    print(header)
    print()

    sample = []  # sample 데이터를 담을 배열 생성.
    cnt = 0  # 반복문 돌릴 때, 사용자가 입력한 동 이름이 다수의 데이터 인지를 확인 하기 위함.
    area = input('동 이름 입력 >> ')

    try:
        for row in data:
            if area in row[0]:  # csv 파일의 모든 행의 0번째 요소값이 입력한 동 이름을 포함 하면
                inputInfo = np.array(row[0])
                print(inputInfo)  # 콘솔창에 출력 하기.
                for v in row[3:]:
                    sample.append(int(v.replace(',', '')))
                cnt += 1
    except Exception:
        pass

    if cnt > 1:  # 입력한 동 이름을 가진 동이 여러 개인 경우
        print('해당 이름을 가진 동이 여러개 입니다 !')
        print('정확 하게 입력해주세요 !')
    elif cnt == 0:  # 입력한 동 이름을 가진 동이 없는 경우
        print('해당 이름을 가진 동은 없습니다 !')
        print('다시 입력하세요 !')

# print(sample)  # 콘솔창에 출력 하기.

if cnt == 1:  # 입력한 동 이름을 가진 동이 딱 1개인 경우.

    fontPath = 'C:/Windows/Fonts/malgun.ttf'  # 폰트 경로 설정.
    font = fm.FontProperties(fname=fontPath).get_name()
    rc('font', family=font)

    plt.plot(sample)
    plt.xticks([0, 2, 4, 6, 8, 10])
    plt.yticks([0, 2000, 4000, 6000, 8000, 10000])
    plt.title('Graph')
    plt.show()

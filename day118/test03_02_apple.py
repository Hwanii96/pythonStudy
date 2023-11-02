import csv

import matplotlib.pyplot as plt

with open('apple.csv', 'r') as file:
    data = csv.reader(file)
    header = next(data)
    print(header)
    print()

    sample = []
    area = input('출력할 지역 입력 >> ')
    for row in data:
        if area in row[0]:
            for v in row[3:]:
                sample.append(int(v.replace(',', '')))

                # sample.append(int(v))
                # 실무에서는 함수를 사용 해서 데이터를 바꾸지 않는다. 비효율 !
                # 그러면 어떻게 해야 할까 ?
                # 데이터 자체를 변경 한다.
                # => 액셀 파일 에서 , 를 제거 !
                # 그렇게 , 콤마를 모두 지우면, 콤마가 없는 문자열 데이터는,
                # int 형으로 형변환이 가능 하므로,
                # sample.append(int(v)) 이렇게 작성 할 수 있게 된다.
                # 바꾸려 했는데 액셀 기한이 만료 되서 수정을 못함 ㄷㄷ

print(sample)

plt.plot(sample)
plt.show()

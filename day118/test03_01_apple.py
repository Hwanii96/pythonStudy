import csv

with open('apple.csv', 'r') as file:
    data = csv.reader(file)
    header = next(data)
    print(header)
    print()

    i = 0;
    for row in data:
        i += 1
        if (i == 5):
            break  # 데이터가 많아서 반드시 해줘야 함 !
        print(row)
        print()

        area = input('출력할 지역 입력 >>')
        for row in data:
            if area in row[0]:  # area가 들어 있으면, 행정 구역에 포함된 문자열 이라면
                print(row)
                print()

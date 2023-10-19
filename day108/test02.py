# 첫번째 문제
"""
aList = ['사과', 12000, '바나나', 3900, '키위', 5400]
aList.txt 를 생성 하세요.
사과는(은) 12000원 입니다.
"""

# for i in range(0, len(aList), 2):
# 자바로 따지면 for(int i = 0; i < aList.size(); i += 2) 와 동일 하다.

aList = ['사과', 1200, '바나나', 3900, '키위', 5400]

with open('aList.txt', 'wt') as file:
    for i in range(0, len(aList), 2):  # 리스트에서 인덱스를 2씩 증가 하도록 하기.
        fruit = aList[i]
        price = aList[i + 1]
        message = f'{fruit}는(은) {price}원 입니다. \n'
        file.write(message)

with open('aList.txt', 'rt') as file:
    textFile = file.read()
    print(textFile)

# f 를 명시 하고 작은 따옴표 내부에 {} 중괄호 안에 변수 이름을 넣으면 변수의 값을 문자열에 삽입 할 수 있다.
# 근데 실제로 문자열로 변하지는 않는다.


# 두번째 문제
"""
bList.txt 파일이 있습니다.
[홍길동] [남]
[김아리] [여]
[쉔] [남]
[모르가나] [여]
.
.
화면 에서 남자는 ㅁ명, 여자는 ㅁ명 입니다. 로 나오도록 하기.
"""

with open('bList.txt', 'at') as file:
    while True:
        print('예시 : [홍길동] [남]')
        text = input('입력 :')
        if not text:  # 종료 조건
            break
        file.write(text + '\n')

with open('bList.txt', 'rt') as file:
    bList = file.read()  # read() 만 작성 하면 해당 파일의 전체를 읽어 오는 메서드.
    print('bList.txt : ', bList)
    print('====================')

bList_male_count = bList.count('[남]')  # count() 함수를 사용해서 특정 문자열을 인식 해서 계산 하기.
bList_female_count = bList.count('[여]')

print(f'남자는 {bList_male_count}명, 여자는 {bList_female_count}명 입니다.')

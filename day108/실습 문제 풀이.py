"""
문제 1
aList = ['사과',12000,'바나나',3900,'키위',5400]
aList.txt를 생성해 주세요.
사과는(은) 12000원 입니다.
"""

cList = ['사과', 12000, '바나나', 3900, '키위', 5400]

with open('cList.txt', 'wt') as file:
    for i in range(0, len(cList), 2):
        file.write(cList[i] + '는(은) ')
        file.write(str(cList[i + 1]) + '원 입니다.\n')
    print('aList.txt를 생성 했습니다 !')

"""
문제 2
bList.txt 파일이 있습니다.
[홍길동][남]
[아리][여]
[쉔][남]
[모르가나][여]
.
.
.
파이썬 쉘 화면 에서
남자는 ㅁ명, 여자는 ㅁ명 입니다.
"""

mCnt = 0
fCnt = 0

with open('dList.txt', 'rt') as file:
    while True:
        tmp = file.readline()
        if tmp == '':
            break

        # 데이터 추출 및 정제 == 데이터 가공
        i = tmp.index(']') + 2
        tmp = tmp[i:i + 1]
        if tmp == '남':
            mCnt += 1
        else:
            fCnt += 1
    print('남자는 %d명, 여자는 %d명 입니다.' % (mCnt, fCnt))

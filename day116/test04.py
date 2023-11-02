'''
1. CSV 파일로 데이터 가공
2. 올바른 패키지를 활용하여 데이터 분석
   matplotlib 패키지
      그래프 출력
   numpy 패키지
      배열의 처리
   pandas 판다스
      데이터 입력 및 가공

python -m pip install --upgrade pip
pip install matplotlib
pip install numpy
'''

import numpy as np
import random

'''
# 1. 파이썬에서는 리스트 != 배열
# 2. 계산(연산)을 할때에는 배열 > 리스트
a = np.array( [ [2,3,4], [5,1,7] ] )
print(a)
# 1번 학생의 국어==2점, 영어==3점, 수학==4점
# 2번 학생의 국어==5점, 영어==1점, 수학==7점
print(a[0][1]) # 1번학생의 영어점수볼래

a.shape # 배열의 전체 행,열을 출력
a.dtype # 배열에 저장된 데이터의 타입을 출력
a.astype('float64') # 배열에 저장된 데이터의 타입을 변환
np.sum(a) # 배열의 모든 요소를 더함
np.zeros( (2,3) ) # [0.] 0 데이터를 가지는 배열을 생성
np.ones( (2,3) ) # [1.] 1 데이터를 가지는 배열을 생성
np.arange(1,5) # [1,2,3,4] 데이터를 가지는 배열을 생성
a+b a*b # 배열끼리 연산시 행,열을 맞춰주는 것을 권장 (브로드캐스팅)
'''

'''
학생1
   국어   50   60
   영어   12   13
   수학   10   20
학생2
   국어   50   60
   영어   12   13
   수학   10   20
학생3
   국어   50   60
   영어   12   13
   수학   10   20
'''

studentList = []
for i in range(3):
    kList = []
    for j in range(2):
        kList.append(random.randint(0, 100))
    eList = []
    for j in range(2):
        eList.append(random.randint(0, 100))
    mList = []
    for j in range(2):
        mList.append(random.randint(0, 100))

    student = np.array([kList, eList, mList])
    studentList.append(student)
print(studentList)

print()
print()
print()

### 과제1
##### 단, 점수는 0~100점 랜덤으로 저장해주세요!~~
####### 파이썬 어플의 경우 "가독성", 코테의 경우 "성능"(1중, 최대 2중 for문까지만 허용!)

studentNum = 0
testNameList = ['중간고사', '기말고사']
subjectNameList = ['국어', '영어', '수학']
for student in studentList:
    studentNum += 1

    subjectNum = -1  ###
    for subject in student:
        subjectNum += 1
        testNum = -1  ###
        for test in subject:
            testNum += 1
            print(
                str(studentNum) + '번 학생의 ' + testNameList[testNum] + ' ' + subjectNameList[subjectNum] + ' 점수는 ' + str(
                    test) + '점 입니다.')

    print()

print()
print()
print()

### 과제2
##### 모든 학생들의 중간·기말고사 국어 평균 점수는 42.67점 입니다.
##### 국어/영어/수학 중에서 입력>> 잘못된 입력
##### 제대로 입력해주세요!
##### 국어/영어/수학 중에서 입력>> 수학
##### 수학 시험 1등은 1번 학생 입니다.

total = 0
for v in studentList:
    total += np.sum(v[0])  ###
##print(total)
print('모든 학생들의 중간·기말고사 국어 평균 점수는 %.2f점 입니다.' % (total / 6))

while True:
    subjectName = input('국어/영어/수학 중에서 입력>> ')
    if subjectName in subjectNameList:
        break
    print('제대로 입력해주세요!')

tmpList = []  # 최대값들의 모임 리스트
for v in studentList:
    index = subjectNameList.index(subjectName)
    subjectTotal = v[index]
    tmpMax = np.sum(subjectTotal)
    tmpList.append(tmpMax)

print(subjectName + ' 시험 1등은 ' + str(tmpList.index(max(tmpList)) + 1) + '번 학생 입니다.')

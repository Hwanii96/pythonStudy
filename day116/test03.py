"""
과제 1
단, 점수는 0 ~ 100점 랜덤으로 저장.

1번 학생의 중간고사 국어 점수는 27점 입니다.
1번 학생의 기말고사 국어 점수는 68점 입니다.
1번 학생의 중간고사 영어 점수는 49점 입니다.
1번 학생의 기말고사 영어 점수는 56점 입니다.
..
..
3번 학생의 중간고사 국어 점수는 .. 입니다.
3번 학생의 기말고사 국어 점수는 .. 입니다.
..
..
"""

"""
과제2
모든 학생들의 중간 · 기말고사 국어 평균 점수는 42.67점 입니다.
국어 / 영어 / 수학 중에서 입력 >> ㅁㄴㅇㄹ
제대로 입력해주세요!
국어 / 영어 / 수학 중에서 입력 >> 수학
수학 시험 1등은 1번 학생 입니다.
"""

# 파이썬 어플의 경우 "가독성 중요"
# 코딩테스트의 경우 "성능 중요" => 1중 ~ 2중 까지만 for문 허용.

import numpy as np
import random as ra

studentList = []

for i in range(3):
    kList = []  # 국어 점수 ( 중간 (0 번째 요소) / 기말 (1 번째 요소) )
    for j in range(2):
        randNum = ra.randint(0, 100)
        kList.append(randNum)

    eList = []  # 영어 점수
    for j in range(2):
        randNum = ra.randint(0, 100)
        eList.append(randNum)

    mList = []  # 수학 점수
    for j in range(2):
        randNum = ra.randint(0, 100)
        mList.append(randNum)

    student = np.array([kList, eList, mList])
    studentList.append(student)

for data in studentList:
    print(data)

examList = ['중간고사', '기말고사']
subjectList = ['국어', '영어', '수학']

studentNum = 0  # 카운팅을 위한 변수 선언.
for student in studentList:  # forEach 문
    studentNum += 1  # studentNum = studentNum + 1

    print('test1')
    print(student)

    subjectNum = -1  # 인덱스니까 for문 루프 끝나면 첫번째 인덱스가 0번째 인덱스가 되어야 함.
    for subject in student:
        subjectNum += 1

        print('test2')
        print(subject)

        examNum = -1  # 인덱스니까 for문 루프 끝나면 첫번째 인덱스가 0번째 인덱스가 되어야 함.
        for exam in subject:
            examNum += 1

            print('test3')
            print(exam)

            print(str(studentNum) + '번 학생의 ' + examList[examNum] + ' ' + subjectList[subjectNum] + ' 점수는 ' + str(
                exam) + '점 입니다.')

    print()

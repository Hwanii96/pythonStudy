import numpy as np

"""
학생1
    국어  50  60
    영어  12  13
    수학  10  20

학생2
    국어  50  60
    영어  12  13
    수학  10  20

학생3
    국어  50  60
    영어  12  13
    수학  10  20
"""

studentList = []
for i in range(3):
    kList = []
    for j in range(2):  # 국어 X 2
        score = int(input('국어 점수 입력 >> '))
        kList.append(score)

    eList = []
    for j in range(2):  # 영어 X 2
        score = int(input('영어 점수 입력 >> '))
        eList.append(score)

    mList = []
    for j in range(2):  # 수학 X 2
        score = int(input('수학 점수 입력 >> '))
        mList.append(score)

    student = np.array([kList, eList, mList])
    studentList.append(student)

print(studentList)

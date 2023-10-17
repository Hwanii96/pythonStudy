# 실습 문제

"""
1.  랜덤 으로 1 ~ 5 사이의 정수를 생성 해주세요.

2.  만약 랜덤값이 3 이면
    -> 3개의 정수를 사용자가 직접 입력 합니다.
    이때 입력 하는 값은 0 이상 100 이하의 정수 이며,
    이 입력은 절대 틀리지 않습니다.

3.  50 60 55 입력시,
    60점 1등 2번학생
    50점 3등 1번학생
    이렇게 출력 해주세요.
    동점자 존재시 가장 마지막 학생을 출력 합니다.

4.  사용자 정의 함수 func() 을 사용 하여
    3명의 평균 점수는 55.0점 입니다.
    이렇게 출력 해주세요.
"""

from random import randrange as rr

rNum = rr(1, 6)
print('랜덤 수는', rNum, '입니다.')
print('학생 점수', rNum, '번을 입력 하세요.')

studentScoreList = []


def printFunc():
    print('점수는 0점 에서 100점 사이로 입력 해주세요.')


for i in range(rNum):

    while True:
        num = int(input('학생 점수 %d 번을 입력하세요: ' % (i + 1)))

        if 0 <= num <= 100:
            studentScoreList.append(num)
            print('log : ', studentScoreList)
            break  # 올바른 입력이 들어올 때까지 계속 반복
        else:
            printFunc()

print('log : studentScoreList : ', studentScoreList)

highScore = max(studentScoreList)
print('log : highScore : ', highScore)

# 점수를 내림차순 으로 정렬
sorted_scoreList = sorted(studentScoreList, reverse=True)  # reverse=True 를 사용해서 내림차순으로 정렬.
print('log : sorted_scoreList : ', sorted_scoreList)

for i, score in enumerate(sorted_scoreList, start=1):  # enumerate() 함수 - 순회 가능한 객체를 순회 하면서 요소와 인덱스 값을 반환.
    print(f"{score}점 {i}등")


def avgCal():
    studentScoreSum = sum(studentScoreList)
    studentScoreListLength = len(studentScoreList)
    studentAvg = studentScoreSum / studentScoreListLength  # 평균 = 학생 점수 총합 / 학생 점수 리스트의 길이

    return f"{studentScoreListLength}명의 평균 점수는 {studentAvg:.1f}점 입니다."


avgCalResult = avgCal()
print(avgCalResult)

# 함수에 반환값이 없으면 print() 를 하면 None 이 뜨게 된다.
# 함수에 return 값을 직접 명시해주면 None 이 사라 지게 된다.

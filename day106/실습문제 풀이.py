import random as r


def func(aList):
    return sum(aList) / len(aList)


randNum = r.randrange(1, 6)

print('randNum : ', randNum)

numList = []

for i in range(randNum):
    num = int(input('0 이상 100 이하의 정수 입력 : '))
    numList.append(num)

print(numList)

avg = func(numList)
print('%d명의 평균 점수는 %.1f점 입니다.' % (randNum, avg))

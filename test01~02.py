# print('hello') # 문자열 'hello' 를 출력.

a = 'hello'  # 변수 a에 문자열 'hello' 를 저장.

# 문자열 == 문자 + 배열 -> index 개념이 존재
# 내장된 기능이 매우 많아서 변수명[index], 변수명[index - 1], 변수명[index:index] 등을 지원
print(a[0])  # 'h'
print(a[1])  # 'e'
print(a[2])  # 'l'
print(a[3])  # 'l'
print(a[4])  # 'o'

print(a[-1])  # 'o' -> 역순 index

print(a[1:4])  # 'ell' -> from ~ to == 1 <= x < 4 == 1, 2, 3

# ============================================================

"""

여러줄
주석

"""

# ============================================================

# alt + 3 : 해당 영역 전체 주석 처리 (Python IDLE 기준)
# alt + 4 : 해당 영역 전체 주석 해제 처리 (Python IDLE 기준)

# ============================================================

a = [10, 11, 12]  # List (배열리스트)

b = [10, 11.2, 'apple']  # 타입 제네릭을 설정해주지 않으면 여러 타입의 데이터 저장 가능 (하지만 이렇게 안함)

list = [10, 20, 30, 40, 50, 60, 70]

fromToList = list[3:6]
print('fromToList : ', fromToList)  # 40, 50, 60

fromToListReverse = list[-2:]
print('fromToListReverse : ', fromToListReverse)  # 60, 70

fromToListAll = list[:7]
print('fromToListAll : ', fromToListAll)  # 10, 20, 30, 40, 50, 60, 70

# ============================================================

c = (10, 11, 12)  # 튜플 == tuple

d = (10, 11.2, 'apple')  # 값 변경 불가능

e = tuple(c)  # 타입 변환 함수 활용 가능

# ============================================================

f = {10, 11, 12}  # 집합 == set / 데이터 중복 제거용 으로 사용 / 순서 X

# ============================================================

g = {'a': 'apple', 'b': 'banana', 'c': 'kiwi'}  # 딕셔너리 == dict -> 자바의 map 컬렉션과 유사

print('g : ', g)  # {'a': 'apple', 'b': 'banana', 'c': 'kiwi'}

print('apple : ', g['a'])  # apple :  apple
print('banana : ', g['b'])  # banana :  banana
print('kiwi : ', g['c'])  # kiwi :  kiwi

# ============================================================

ten = 10
twenty = 20

print('ten + twenty = ' + str(ten + twenty) + ' 입니다.')

print('ten + twenty = %d 입니다.' % (ten + twenty))  # 포맷팅 출력 방식 (문법이 이러하다)

# ============================================================

# input() 함수로 입력 받는 데이터는 모두 문자열 데이터 이다.
# 정수를 원하면 input() 함수에 int로 래핑 한다.

sc = input('정수 입력 : ')
print(sc)
print(type(sc))  # <class 'str'>

sc2 = int(input('정수 입력 : '))
print(sc2)
print(type(sc2))  # <class 'int'>

# ============================================================

# if-else 문

arrList = [10, 20, 30]

# 20이 있나요 ? 를 not 으로 부정
if 20 not in arrList:
    print('있음')
else:
    print('없음')

# 결과 -> 없음

# ============================================================

# 연습 문제 1
# 두자리 정수를 입력 하세요.
# 45
# 십의 자리 4
# 일의 자리 5

num = (int(input('두자리 정수를 입력 하세요 >> ')))
print('입력한 두자리 정수 : ', num)

ten = num // 10
one = num % 10

print('십의 자리 : ', ten)
print('일의 자리 : ', one)

# ============================================================

# 연습 문제 2 => 풀이 방법 A
# 점수를 입력 받으세요.
# 1번 점수 : 20
# 2번 점수 : 30
# 3번 점수 : 40
# 평균 __.__ 점이고, 합격 입니다.
# 만약 평균이 60.0점 미만 이라면 불합격.

total = 0

for i in range(3):
    num = int(input('%d 번 점수 : ' % (i + 1)))
    total += num

print('평균 %.2f점 이고, ' % round(total / 3, 2))

if total / 3 >= 60.0:
    print('합격 입니다.')
else:
    print('불합격 입니다.')

# ============================================================

# 연습 문제 2 => 풀이 방법 B
# 점수를 입력 받으세요.
# 1번 점수 : 20
# 2번 점수 : 30
# 3번 점수 : 40
# 평균 __.__ 점이고, 합격 입니다.
# 만약 평균이 60.0점 미만 이라면 불합격.

score = []

for i in range(3):
    score.append(int(input('%d번 점수 : ' % (i + 1))))

avg = sum(score) / len(score)

print('평균 %.2f점 이고, ' % avg)

if avg >= 60.0:
    print('합격 입니다.')
else:
    print('불합격 입니다.')

# ============================================================

# 자바의 for 문과 유사한 문법

for i in range(3):
    print('i : ', i)  # 0, 1, 2

    # ============================================================

    # 자바의 for each 문과 유사한 문법

testList = [10, 20, 30]

for datas in testList:
    print('testList : ', datas)  # 10, 20, 30

# ============================================================

testList2 = [10, 20, 30]

testList2.append(5)  # 10, 20, 30, 5
print('testList2 : ', testList2)

testList2.insert(0, 100)  # 100, 10, 20, 30, 5
print('testList2 : ', testList2)

sortedTestList2 = sorted(testList2)  # 5, 10, 20, 30, 100
print('sortedTestList2 : ', sortedTestList2)

# 함수의 3요소 == 메서드 시그니쳐 (JAVA)

# 인자 == 인수 == input == 입력값 == 매개변수 == args == 파라미터
# 반환값 == 리턴값 == return == 출력값 == 결과값 == output
# 함수의 기능 == 함수명

# 함수는 보라색 이다.
# 함수명은 함수의 기능을 유추 할 수 있게 만든다.
"""
type()
print()
range()
"""


# 사용자 정의 함수 (원래 파이썬에 존재하는 함수는 내장 함수 라고 한다)
# def 키워드를 사용해서 함수를 선언 == 정의
# 함수를 사용 하려면 함수를 호출 해야 한다.
def printApple():
    print('apple')


printApple()


# 함수의 장점
# 코드 재사용성 용이
# 유지보수 용이
# 오류의 파급효과 절감 (잘 만들어진 함수를 재사용 하기 때문에 오류가 날 가능성이 낮아진다)
# 개발 시간 및 비용 절감 (이미 만들어진 로그인 SNS API를 가져와서 사용 하는 개념)

def funcA(a):
    print('a = ', a)


def funcB(b):
    print('b = ', b)
    return b


# funcB()  # TypeError: funcB() missing 1 required positional argument: 'b' -> 필수적으로 인자 1개가 필요 !

funcB(-13)  # 에코 현상 왜 안 일어남 ? (원래 반환값을 저장할 공간을 주지 않으면 값이 한번 더 보여지는 에코 현상이 발생)

banana = funcB(-13)


def funcC():
    return 1234


# def funcD():
#     for i in range(10): # IndentationError: expected an indented block after 'for' statement on line 51

def funcD():
    for i in range(10):
        pass  # 아직 미완성인 함수 일 때 pass 키워드를 명시 해서 에러가 발생 하지 않도록 할 수 있다.


def funcE(*a):  # 애스터리스크 -> * => 별이 붙어 있는 매개변수를 가변 매개 변수 라고 한다.
    print(a)
    print(type(a))  # 가변 매개 변수는 tuple == 튜플 타입으로 넘어 오게 된다.

    for data in a:
        print(data)


funcE(1, 2, 3, 4)
funcE('apple', 1234, 3.14)


def funcF(a, b, c=123):  # 디폴트 매개변수 (무한대로 설정이 가능 하다)
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)


funcF(-1, -2, -3)
print()
funcF(-1, -2)
print()

# 파이썬의 print() 함수는 디폴트로 자바의 println() 처럼 줄바꿈이 된다.
print('안녕하세요 !')
print('파이썬 2일차 입니다 ㅎ_ㅎ')
print('ㅎㅎ')

# 줄바꿈을 원치 않으면 아래와 같이 하면 된다. 즉, print() 함수의 매개변수 로는 end 라는 인자값이 있다.
# end는 디폴트 매개변수 값으로 '\n' 을 갖고 있었다는 것을 알 수 있다.
print('안녕하세요 ! ', end='')
print('파이썬 2일차 입니다 ㅎ_ㅎ')
print('ㅎㅎ')

# 예외 처리

# 모든 프로그램은 비정상 종료가 되지 않도록 예외 처리를 반드시 해줘야 한다.
# 설령 비정상 종료가 되더라도 사용자에게 어떤 이유로 인해 그렇게 되었는지를 안내해줄 수 있어야 한다.

# 2 / 0
# ZeroDivisionError: division by zero

"""
try:
    예외가 발생 할 수도 있는 코드
except:
    예외 발생시 수행할 코드
"""

"""
try:
    num = int(input('정수 입력 : '))
    print('입력한 정수는 %d 입니다.' % num)
except:
    print('정수만 입력해 주세요 !')
"""

try:
    num = int(input('정수 입력 : '))
    print('10 / %d = %d' % (num, 10 / num))
except:
    print('정수만 입력해 주세요 !')

# 그런데 특정 예외를 작성 할 수 있다. 그리고 저렇게 작성 하지 않는다.
# except 특정 예외 클래스명:
# 문법 으로 작성 하고, 여러개의 특정 예외를 작성 하고 싶으면 except 다중으로 작성 하면 된다.
# 그런데 모든 예외를 처리 하고 싶으면 모든 예외의 최고 조상인 Exception 을 작성 하면 된다.

"""
try:
    num = int(input('정수 입력 : '))
    print('10 / %d = %d' % (num, 10 / num))
except ValueError:
    print('정수만 입력해 주세요 !')
except ZeroDivisionError:
    print('0 으로는 나눌 수 없습니다 !')
except Exception:
    print('처리 하지 못하는 예외 입니다 !')
finally:
    print('try 이던, catch 이던, 반드시 행해 져야 할 때 ~')
"""

# 자바의 finally 문법과 같이, 파이썬에도 finally 가 존재 한다.

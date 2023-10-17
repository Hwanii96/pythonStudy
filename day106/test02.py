# 모듈 module == 라이브러리 => 자바의 클래스 역할
# .py 파이썬 파일
# 모듈 module 이라는 표현을 사용 할 때는 아래와 같다.
# 누군가 기능을 바로 사용 할 수 있도록 미리 구현해놓은 .py 파일을 모듈 이라고 하고, 라이브러리 라고도 볼 수 있다.

# import 키워드를 사용 해서 math (모듈) 안에 있는 것들을 사용 하기.
# 별도의 라이브러리 설치 필요 없이 사용 할 수 있는 모듈을 '표준 모듈' 이라고 한다.
# 설치 해야 사용 가능한 모듈을 '외부 모듈' == '패키지' == 'package' 라고 한다.
import math

print('============================')
print(math.pi)
print(math.pow(2, 5))

# 가져올 모듈의 크기가 너무 크다고 가정해보자.
# 그 안에 몇가지 함수만 사용할 예정 인데 모두 가져오는것은 비효율적이지 않겠는가 ?
# 이런 경우에는 from '모듈명' import '사용할 함수명'
# 으로 작성 하면 된다.

from random import randrange

print('============================')
print(randrange(10))  # 0 ~ 9 범위에서 랜덤한 숫자 1개
print(randrange(1, 10))  # 1 ~ 9 범위에서 랜덤한 숫자 1개

# 사용할 함수명을 여러개 작성 할 수도 있다.
from random import randrange, choice

print('============================')
print(randrange(10))
print(randrange(1, 10))
print(choice([10, 11, 13, 15, 23]))

# 모듈명이 너무 길거나 또는 가독성을 위해 모듈명에 별칭을 부여 할 수도 있다. (alias == 별칭 == 별명)
import random as r

print('============================')
r = r.randrange(10)
print(r)

# 모듈 안에 사용할 함수명에도 별칭을 부여 할 수도 있다. (alias == 별칭 == 별명)
from random import randrange as rr

print('============================')
rr = rr(1, 10)
print(rr)

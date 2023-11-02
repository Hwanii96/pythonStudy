import matplotlib.pyplot as plt  # pyplot : 그래프 그리기 위한 모듈
import random

dice = []

for i in range(100000):
    rand = random.randint(1, 6)
    dice.append(rand)

plt.hist(dice, bins=6)
plt.show()

# 요놈을 numpy 로 작성 하기
# numpy 로 하면, for 문 사라 지고, 배열도 사용 하지 않아도 된다.
# 성능에 우수
# -> test02.py

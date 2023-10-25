# 데이터 시각화

"""

matplotlib 라이브러리
pyplot 모듈
외부 모듈을 설치 == pip

cmd 창에 pip install matplotlib

(파이참을 사용 하면, import matplotlib 라고 검색 하고 alt + enter 으로 라이브러리 설치)

만약에 아래와 같은 안내 멘트가 나온 다면

pip NOT FOUND == PATH 설정 관련 문제 이다

"""

import matplotlib.pyplot as plt

aList = [10, 20, 30, 40]
bList = [20, 40, 10, 30]

# plt.plot(aList)  # 리스트 데이터를 그래프화 해줘 ~
# plt.plot(bList)  # 리스트 데이터를 그래프화 해줘 ~
# plt.plot(aList, bList)  # 리스트 데이터를 그래프화 해줘 ~

plt.title('no hangul ^~^')  # 캡션 추가 하기 (한글 지원은 안해서 영어로만 가능 / 캡션 : 그래프의 제목)
plt.plot(aList, color='hotpink', label='aList')
plt.plot(bList, ls='--', label='bList')  # 그래프 스타일 변경도 가능 하다 => ls (line style)
plt.legend()  # label => 범례 추가 하기 (설명)
plt.show()

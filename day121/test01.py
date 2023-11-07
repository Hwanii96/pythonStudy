import pandas as pd
import numpy as np

"""
기본 문법
csv 파일
라이브러리
matplotlib (데이터 시각화) / numpy (리스트 != 배열 ! => 배열을 다루기 위한 라이브러리)
pandas (데이터 프레임을 다루는 라이브러리) =>
"""

"""
pandas
데이터 프레임 == 테이블 형태의 데이터 == 2차원 배열 !
2차원 배열 : 행과 열 을 가진 구조 이다 !
행 == index == 인덱스
열 = column == 칼럼
"""

index = pd.date_range('11/1/2023', periods=8)
# 11월 1일 부터 8일 까지 총 8개의 행 == index 을 생성 하기.

df = pd.DataFrame(np.random.rand(8, 3), index=index, columns=list('ABC'))
# numpy 라이브러리로 8행 3열 짜리 랜덤 데이터 생성
# 행 => index, 열 => 'ABC' 로 설정 하기.

print(df)

print()

print(df['C'])

print()

df2 = df[df['A'] < 0.6]

print(df2)

print()

print(df['A'] >= 0.5)

df['D'] = df['A'] / df['B']  # 새로운 데이터를 만들 수도 있음. (데이터 프레임을 다룰 때 나누기 연산 많이 사용)

print(df)  # 그리고 그 결과를 다시 csv 파일에 넣기.

df.to_csv('final.csv')  # 이렇게 결과물을 csv 파일에 넣는것을 많이 사용 한다.

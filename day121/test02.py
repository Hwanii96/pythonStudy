import pandas as pd

# 보통은 2차원 배열 데이터가 존재 하는 상황에, 데이터 프레임을 다룬다.
# 그리고 데이터를 보관 하거나 다룰때, dict (딕셔너리) 를 많이 사용 한다.

data = {  # 2차원 배열을 생성 할 때, 중괄호 블럭을 사용 한다.
    'Name': ['Alice', 'Bob', 'David'],
    'Score': [30, 88, 59],
    'City': ['Chicago', 'New York', 'Los Angeles']
}

# pandas로 데이터 프레임 만들기 => data frame

df = pd.DataFrame(data)

print(df)

print()

print(df['Name'])  # 특정 열을 출력 하는 문법

print()

print(df.loc[0])  # 특정 행을 출력 하기

print()

print(df[df['Score'] > 50])  # 조건을 만족 하는 데이터를 출력 하는 문법

print()

df['Age'] = [20, 22, 21]  # 데이터 추가 하기

print(df)

print()

ndata = {'Name': 'Anna', 'Score': 85, 'City': 'Seoul', 'Age': 30}  # 데이터 만들기

# dataframe 에 36 번째 라인 에서 만든 데이터를 추가 하기
df = df._append(ndata, ignore_index=True)
# 인덱스를 재설정 해서 새로운 행이 최신 행으로 추가 될 수 있다

print(df)

# 행과 열 을 잘 고려 해서 하면 된다.

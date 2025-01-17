import pandas as pd

data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, 35, 29],
    '직업': ['학생', '엔지니어', '디자이너']
}

df = pd.DataFrame(data)

print("데이터프레임:")
print(df)

print("\n데이터프레임 정보:")
print(df.info())

print("\n데이터프레임 통계:")
print(df.describe())

data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, 35, 29],
    '직업': ['학생', '엔지니어', '디자이너']
}
df = pd.DataFrame(data)

print("이름 열 선택:")
print(df['이름'])

print("\n이름과 나이 열 선택:")
print(df[['이름', '나이']])

print("\n첫 번째 행 선택:")
print(df.iloc[0])

print("\n나이가 30 이상인 사람들:")
print(df[df['나이'] >= 30])

data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, 35, 29],
    '직업': ['학생', '엔지니어', '디자이너']
}
df = pd.DataFrame(data)

df['성별'] = ['남', '남', '여']
print("새로운 열 추가:")
print(df)

df['나이'] = df['나이'] + 1
print("\n나이 수정:")
print(df)

new_row = {'이름': '최민수', '나이': 28, '직업': '의사', '성별': '남'}
df = df.append(new_row, ignore_index=True)
print("\n행 추가:")
print(df)

data = {
    '이름': ['홍길동', '김철수', '이영희', '최민수'],
    '나이': [23, 35, 29, 28],
    '직업': ['학생', '엔지니어', '디자이너', '의사']
}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='나이')
print("나이 순 오름차순 정렬:")
print(sorted_df)

grouped_df = df.groupby('직업')['나이'].mean()
print("\n직업별 평균 나이:")
print(grouped_df)

data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, 35, 29],
    '직업': ['학생', '엔지니어', '디자이너']
}
df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)

df_from_csv = pd.read_csv('data.csv')
print("\nCSV 파일에서 읽은 데이터:")
print(df_from_csv)

import numpy as np

data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [23, np.nan, 29],
    '직업': [np.nan, '엔지니어', '디자이너']
}
df = pd.DataFrame(data)

print("결측치 확인:")
print(df.isnull())

df['나이'] = df['나이'].fillna(df['나이'].mean())
print("\n나이 결측치 처리:")
print(df)

df = df.dropna()
print("\n결측치가 있는 행 제거:")
print(df)

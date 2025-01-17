import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())

import pandas as pd
import numpy as np

data = {'이름': ['홍길동', '김철수', '이영희', np.nan],
        '나이': [23, np.nan, 29, 35],
        '직업': ['학생', '엔지니어', np.nan, '디자이너']}
df = pd.DataFrame(data)

print("결측치 확인:")
print(df.isnull())

df_cleaned = df.dropna()
print("\n결측치 제거된 데이터:")
print(df_cleaned)

df['나이'] = df['나이'].fillna(df['나이'].mean())
print("\n결측치가 평균값으로 대체된 데이터:")
print(df)

import pandas as pd

data = {'이름': ['홍길동', '김철수', '이영희', '홍길동'],
        '나이': [23, 35, 29, 23],
        '직업': ['학생', '엔지니어', '디자이너', '학생']}
df = pd.DataFrame(data)

df_no_duplicates = df.drop_duplicates()
print("\n중복된 행이 제거된 데이터:")
print(df_no_duplicates)

import pandas as pd

data = {'날짜': ['2023-01-01', '2023-01-02', '2023-01-03']}
df = pd.DataFrame(data)

df['날짜'] = pd.to_datetime(df['날짜'])
print("\n날짜 형식으로 변환된 데이터:")
print(df)

import pandas as pd

data = {'직업': ['학생', '엔지니어', '디자이너', '학생']}
df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['직업'])
print("\nOne-Hot Encoding된 데이터:")
print(df_encoded)

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {'나이': [23, 35, 29, 41],
        '소득': [40000, 70000, 50000, 80000]}
df = pd.DataFrame(data)

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

print("\n표준화된 데이터:")
print(df_scaled)

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

data = {'특성1': [1, 2, 3, 4, 5],
        '특성2': [5, 4, 3, 2, 1],
        '특성3': [1, 2, 3, 4, 5],
        '레이블': [0, 1, 0, 1, 0]}
df = pd.DataFrame(data)

X = df[['특성1', '특성2', '특성3']]
y = df['레이블']
selector = SelectKBest(f_classif, k=2)
X_new = selector.fit_transform(X, y)

print("\n선택된 상위 2개 특성:")
print(X_new)

import pandas as pd

data = {'이름': ['홍길동', '김철수', '이영희']}
df = pd.DataFrame(data)

df['이름'] = df['이름'].str.lower()
print("\n소문자로 변환된 이름:")
print(df)

df['이름'] = df['이름'].str.replace('길동', '철수')
print("\n이름 수정 후:")
print(df)

import pandas as pd

df1 = pd.DataFrame({'이름': ['홍길동', '김철수'], '나이': [23, 35]})
df2 = pd.DataFrame({'이름': ['이영희', '최민수'], '나이': [29, 28]})

df_combined = pd.concat([df1, df2], ignore_index=True)
print("\n결합된 데이터프레임:")
print(df_combined)

import pandas as pd

data = {'이름': ['홍길동', '김철수', '이영희', '최민수', '박지민'],
        '나이': [23, 35, 29, 28, 30]}
df = pd.DataFrame(data)

sampled_df = df.sample(n=2)
print("\n랜덤 샘플링된 데이터:")
print(sampled_df)
# 200222 13:34
# 데이터 사이언스
# DataFrame 인덱싱
# 09. 방송사 시청률 받아오기 5

import pandas as pd

df = pd.read_csv(r'C:\Users\hayong\Downloads\broadcast.csv', index_col=0)

# 코드를 작성하세요.
# print(df.loc[(df['시청률'] > 30]) & (df['KBS'] == Yes)

# df = df.loc[df['KBS']>30]
# df = df['KBS']
# df

# 모범 답안은?
boolean_KBS = df['KBS'] > 30
print(df.loc[boolean_KBS, 'KBS'])

"""
먼저 'KBS'에 대한 정보만을 다루기 때문에, 'KBS' column만 사용하면 됩니다.
df['KBS']

그러면 모든 데이터가 다 나오네요.
여기서 불린 연산을 활용해 봅시다.
df['KBS'] > 30

이런 식으로, 30이 넘는지 넘지 않는지 여부가 불린값으로 나옵니다.
이 값을 DataFrame 인덱싱에 활용하면 우리가 원하는 값만 뽑아낼 수 있습니다.
boolean_KBS = df['KBS'] > 30
df.loc[boolean_KBS]

그대로 불린을 넣었더니, 2012년부터 2014년까지 모든 방송사의 데이터가 함께 나오네요.
아래와 같이 코드를 작성하면 우리가 원하는 값만 얻을 수 있습니다.
df.loc[boolean_KBS, 'KBS']
"""
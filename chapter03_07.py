# 200222 13:34
# 데이터 사이언스
# DataFrame 인덱싱
# 10. 방송사 시청률 받아오기 6

import pandas as pd

df = pd.read_csv(r'C:\Users\hayong\Downloads\broadcast.csv', index_col=0)

boolean_df = df['SBS'] < df['TV CHOSUN']
print(df.loc[boolean_df, ['SBS', 'TV CHOSUN']])

# 아이구 잘한다~!
# 찾아서 해내기
# 반복을 통한 숙달
# 이후에는 암기가 자동으로 되어
# 응용, 활용
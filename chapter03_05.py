# 200222 13:34
# 데이터 사이언스
# DataFrame 인덱싱
# DataFrame 조건으로 인덱싱

import pandas as pd
iphone_df = pd.read_csv(r'C:\Users\hayong\Downloads\iphone.csv', index_col=0)

print(iphone_df.loc[[True, False, True, True, False, True, False]])

print()
print(iphone_df['디스플레이'] > 5)

print()
print(iphone_df.loc[iphone_df['디스플레이'] > 5])

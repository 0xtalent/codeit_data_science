# 200222 14:08
# 데이터 사이언스
# DataFrame 인덱싱
# 11. DataFrame 위치로 인덱싱하기

import pandas as pd
iphone_df = pd.read_csv(r'C:\Users\hayong\Downloads\iphone.csv', index_col=0)

print(iphone_df)

print(iphone_df.iloc[2, 4])
print(iphone_df.iloc[[1, 3], [2, 4]])

print()
print(iphone_df.iloc[3:, 1:4])
# row행, column열

# 뭔가 쫌 밀려서 보인다?
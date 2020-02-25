# 200222 11:42
# 데이터 사이언스
# DataFrame 인덱싱

import pandas as pd
iphone_df = pd.read_csv(r'C:\Users\hayong\Downloads\iphone.csv', index_col=0)

print(iphone_df.loc['iPhone X'])
print()
print(iphone_df.loc[['iPhone X', 'iPhone 8']])
print()
print(iphone_df['Face ID'])
print()
print(iphone_df[['Face ID', '출시일', '메모리']])

print()
print(iphone_df['메모리':'Face ID'])

print()
print(iphone_df.loc[:, '메모리':'Face ID'])

# 왜 [[]] 안함?
# 여기서 부터 저기까지 니까
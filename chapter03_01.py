# 200222 08:23
# 데이터 사이언스
# DataFrame 인덱싱

import pandas as pd
iphone_df = pd.read_csv(r'C:\Users\hayong\Downloads\iphone.csv', index_col=0)
print(iphone_df)

print()
print(iphone_df.loc['iPhone 8', '메모리'])

print()
print(iphone_df.loc['iPhone X', :])
print(type(iphone_df.loc['iPhone X', :]))

print()
print(iphone_df.loc[:, '출시일'])

print()
print(iphone_df['출시일'])

# import pandas as pd

# df = pd.read_csv('data/broadcast.csv', index_col=0)

# # 코드를 작성하세요.
# df.loc[2016, 'KBS']

"""
DataFrame에서 인덱싱을 통해 값을 받아오기 위해서는 loc 메소드를 사용하면 됩니다.
여기서 우리가 찾으려는 값의 row(행)는 2016이고 column(열)은 'KBS'입니다.
"""
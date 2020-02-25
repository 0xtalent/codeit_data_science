# 200222 14:33
# 데이터 사이언스
# 데이터 변형하기

import pandas as pd
from tabulate import tabulate

iphone_df = pd.read_csv(r'C:\Users\hayong\Downloads\iphone.csv', index_col=0)

print(tabulate(iphone_df, headers='keys'))

# VSCODE에서 판다스 예쁘게 안보여서 
# https://stackoverflow.com/questions/52225216/pretty-print-a-pandas-dataframe-in-vs-code
# pip install tabulate 설치함
# 그런데도 짤리네
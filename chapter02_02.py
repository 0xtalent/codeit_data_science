# 200222 06:45
# 데이터 사이언스
# Pandas
# B mo님 답변 너무 잘해주신다. 강의 듣고 답변 꼭 확인하면서 진행하기

import pandas as pd

two_dimensional_list = [['hayong', 50, 86], ['kyunghee', 68, 91], ['taekwan', 88, 75], ['joonsu', 88, 75]]
my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])
print(my_df)

print()
print(my_df.columns)
print(my_df.index)

# 진짜 재밌어요~
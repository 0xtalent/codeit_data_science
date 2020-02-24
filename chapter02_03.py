# 200222 07:14
# 데이터 사이언스
# Pandas
# B mo님 답변 너무 잘해주신다. 강의 듣고 답변 꼭 확인하면서 진행하기

import pandas as pd

# 코드를 작성하세요.
two_dimensional_list = [['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'], ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'], ['Harry Potter', 'July 31, 1980', 'Wizard'], ['Ji-Sung Park', 'February 25, 1981', 'Footballer']]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'birthday', 'occupation'])
print(my_df)

# 정답 출력
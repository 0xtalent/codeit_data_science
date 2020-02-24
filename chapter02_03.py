# 200222 07:38
# 데이터 사이언스
# Pandas
# B mo님 답변 너무 잘해주신다. 강의 듣고 답변 꼭 확인하면서 진행하기

import pandas as pd

# 코드를 작성하세요.
two_dimensional_list = [['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'], ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'], ['Harry Potter', 'July 31, 1980', 'Wizard'], ['Ji-Sung Park', 'February 25, 1981', 'Footballer']]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'birthday', 'occupation'])
print(my_df)

"""
모범 답안은 무엇일까요?

1단계: 우선 DataFrame에 들어갈 정보가 담긴 2차원 파이썬 리스트를 만들어 주세요.

celebrities = [
    ['Taylor Swift', 'December 13, 1989', 'Singer-songwriter'],
    ['Aaron Sorkin', 'June 9, 1961', 'Screenwriter'],
    ['Harry Potter', 'July 31, 1980', 'Wizard'],
    ['Ji-Sung Park', 'February 25, 1981', 'Footballer']
]

2단계: 이제 DataFrame을 생성해야겠죠? 
pandas 라이브러리의 DataFrame 함수(생성자)를 사용하면 됩니다.

df = pd.DataFrame(celebrities)

3단계: DataFrame 함수의 columns라는 파라미터로 리스트를 넘겨주면 됩니다.
"""
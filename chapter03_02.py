# 200222 10:34
# 데이터 사이언스
# DataFrame 인덱싱
# 카드사 고객 분석

"""
sam_culture = samsong_df.loc[:,'문화생활비']
hyun_culture = hyundee_df.loc[:, '문화생활비']
sam_day = samsong_df.loc[:, '요일']
final_file = {"day": sam_day, "samsong": sam_culture, "hyundee": hyun_culture}
pd.DataFrame(final_file)

1. 데이터 파악하기
우리가 활용하고 싶은 데이터는 '요일', 
그리고 samsong_df의 '문화생활비', hyundee_df의 '문화생활비' 입니다.

2. 파이썬 사전(dictionary) 만들기
DataFrame을 만드는 여러 방법 중에 파이썬 사전(dictionary)을 활용해 봅시다.

우리가 원하는 세 개의 column은 'day', 'samsong', 'hyundee' 입니다.
{'day': samsong_df['요일'], 
    'samsong': samsong_df['문화생활비'], 
    'hyundee': hyundee_df['문화생활비']}

3. DataFrame 만들기
이제 이 값을 활용해서 DataFrame을 만들면 됩니다.

import pandas as pd

samsong_df = pd.read_csv('data/samsong.csv')
hyundee_df = pd.read_csv('data/hyundee.csv')

combined_df = pd.DataFrame({
    'day': samsong_df['요일'], 
    'samsong': samsong_df['문화생활비'], 
    'hyundee': hyundee_df['문화생활비']
})
combined_df
"""
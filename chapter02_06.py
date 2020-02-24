# 200222 08:23
# 데이터 사이언스
# Pandas
# B mo님 답변 너무 잘해주신다. 강의 듣고 답변 꼭 확인하면서 진행하기

# 가장 인기 있는 아기 이름은?

import pandas as pd
popular_baby_names = pd.read_csv(r'C:\Users\hayong\Downloads\popular_baby_names.csv')
print(popular_baby_names)

# 메가밀리언 로또 당첨 번호

df = pd.read_csv(r'C:\Users\hayong\Downloads\mega_millions.csv', index_col=0)
print(df)

# numpy와 pandas 기초를 공부하며 데이터 사이언스의 매력을 느꼈습니다. 
# 강의 설명도 너무 좋고, 또 짧게 짧게 나눠져 있어서 하나하나 퀘스트를 해결해나가는 
# 재미가 있는 것 같아요. 앞으로도 잘 부탁드려요. 
# 나아가 딥러닝, 머신러닝 소프트웨어 엔지니어, 개발자가 되는 것이 꿈인데 
# 그 시작을 코드잇과 함께 할 수 있어서 좋습니다. 더 열심히 할게요!

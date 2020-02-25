# 200222 17:26
# 데이터 사이언스
# 데이터 변형하기
# 07. 서류 전형 합격 여부

"""
pass_total = df['LC'] + df['RC'] > 600
pass_both = (df['LC'] >= 250) & (df['RC'] >= 250)
df['합격 여부'] = pass_total & pass_both
"""
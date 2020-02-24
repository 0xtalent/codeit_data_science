# 200222 05:41
# 데이터 사이언스
# Numpy

import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1 > 4)

print(array1 % 2 == 0)

# print(array1 % 2 = 0) 이런 실수를 해버렸네ㅋㅋ

booleans = np.array([True, False, True, True, True, True, True, True, False, True])
print(np.where(booleans))

# 흥부부대찌개 목표 일 매출
import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 코드를 작성하세요.
yen_array = np.array(revenue_in_yen)
print(yen_array > 200000)
# np.array 안하면 아래 오류 뜨네/아직은 왜 np.array 해야 되는지 모르겠다
# TypeError: '>' not supported between instances of 'list' and 'int'

# 정답 출력
filter = np.where(yen_array <= 200000)
bad_days_revenue = yen_array[filter]
print(bad_days_revenue)

"""
filter = np.where(yen_array <= 20000)
bad_days_revenue = revenue_in_yen[filter]
print(bad_days_revenue)

이렇게 하면 오류남
np.array 한 거에서 해야 함
"""

"""
[해설 + np.array 왜 하는지]

numpy array의 좋은 점은 리스트 안의 데이터를 반복문 없이 한 번에 분석할 수 있다는 것
우리의 매출이 revenue_in_yen 이라는 변수에 리스트 형태로 들어 있다.

numpy의 도움을 받기 위해서는 numpy array로 만들어 주어야겠죠?
yen_array = np.array(revenue_in_yen)

그리고 주어진 조건에 해당하는 filter를 만들어 줍시다.
우리가 원하는 데이터가 어디에 있는지 확인할 수 있네요.
이 filter를 인덱싱에 활용해주면, 우리가 원하는 결과를 얻을 수 있습니다.

bad_days_revenue = yen_array[filter]
bad_days_revenue # 정답 출력

아래와 같이 where 메소드로 filter를 만들지 않고 바로 인덱싱하는 방법도 있다는 것! 참고하세요.

yen_array = np.array(revenue_in_yen)
bad_days_revenue = yen_array[yen_array < 200000]
bad_days_revenue # 정답 출력
"""
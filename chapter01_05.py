# 200222 06:27
# 데이터 사이언스
# Numpy

"""
최댓값, 최솟값
max 메소드와 min 메소드를 사용하면 numpy array의 최댓값과 최솟값을 구할 수 있습니다.

import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.max()) # 최댓값
print(array1.min()) # 최솟값

평균값
mean 메소드를 사용하면 numpy array의 평균값을 구할 수 있습니다.

import numpy as np

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.mean()) # 평균값

중앙값
median 메소드를 사용하면 중간값을 구할 수 있는데요. 
특이하게 median은 numpy array의 메소드가 아니라 numpy의 메소드입니다.

표준 편차, 분산
표준 편차와 분산은 값들이 평균에서 얼마나 떨어져 있는지 나타내는 지표입니다.

array1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(array1.std()) # 표준 편차
print(array1.var()) # 분산
"""
# 200222 07:49
# 데이터 사이언스
# Pandas
# B mo님 답변 너무 잘해주신다. 강의 듣고 답변 꼭 확인하면서 진행하기

"""
pandas에 담을 수 있는 dtype(데이터 타입) 몇 가지를 살펴봅시다.

int64	정수
float64	소수
object	텍스트
bool	불린(참과 거짓)
datetime64	날짜와 시간
category	카테고리

CSV(Comma-Separated Values): 값들이 쉼표로 나뉘어져 있다.
"""

"""
파이썬 pandas 모듈에서 파일을 불러올 때 
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
오류가 나는 경우가 있습니다.

\U 부분 때문에 유니코드로 인식되는 에러인데요

해결방법은
1. 따옴표 앞에 r을 붙히면 해결됩니다.
2. \를 두개씩 넣어도 해결됩니다.

https://eclipse360.tistory.com/4
"""

# 이건 왜 오류나는겨? 이유를 모르겠네ㅋㅋ
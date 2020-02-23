# 컴퓨터 개론 빠르게 끝내기
# 200224 04:59
# 추상화, retrun과 print의 차이
# 복습 꼭 하기

def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print(print_square(3))

# return 문이 없으면, None이 return 됨
# 즉시 종료하는 것도 알지?

"""
파라미터의 기본값을 설정해두면 함수 호출을 할 때 
파라미터에 해당되는 값을 넘겨주지 않았을 경우, 그 파라미터는 기본값을 갖게 됩니다. 
이런 파라미터를 optional parameter라고 부릅니다.

Optional parameter는 모두 마지막에 있어야 합니다.

x += 1
x *= 2
x -= 3
x /= 2
x %= 7

위와 같이 자주 쓰이는 표현을 간략하게 쓸 수 있게 해 주는 문법을 syntactic sugar라고 합니다.

https://www.codeit.kr/community/threads/10364
"""

def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))

def calculate_change(payment, cost):
    change = payment - cost

    fifty_count = change // 50000
    ten_count = (change % 50000) // 10000
    five_count = (change % 10000) // 5000
    one_count = (change % 5000) // 1000

    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
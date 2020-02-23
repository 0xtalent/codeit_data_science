# 컴퓨터 개론 빠르게 끝내기
# 200223 16:03
# 파이썬 프로그래밍 시작하기

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))

"""
가장 오래된 방식 (% 기호)
print("제 이름은 %s이고 %d살입니다." % (name, age))

현재 가장 많이 쓰는 방식 (format 메소드)
print("제 이름은 {}이고 {}살입니다.".format(name, age))

새로운 방식 (f-string)

name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")
"""

wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * exchange_rate * 1, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * exchange_rate * 5, "원"))

# True or False의 값은 True
# True and False의 값은 False

print(type(4 / 2))
print(type("True"))
print(type(10 <= 7))
print(type(2.0 ** 3))
print(type(2 * 3 == 6))

# 4 / 2는 2.0입니다. 따라서 <class 'int'>가 아니라 <class 'float'>가 출력됩니다.
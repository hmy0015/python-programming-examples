"""
    s = '1.23, 2.4, 3.123'
    문자열 s에 있는 숫자들의 합을 출력하는 프로그램을 작성하시오. (p. 34)
"""
s = '1.23, 2.4, 3.123'
numbers = s.split(',')
sum = 0

for number in numbers:
    sum += float(number)

print(sum)
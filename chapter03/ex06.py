"""
    뉴턴-랩슨을 구현한 코드에서 근을 구할 때 루프의 반복 횟수를 출력한 후 출력값을 참고하여 뉴턴-랩슨과 이분 검색의 효율성을 비교해보시오. (p.43)
"""

epsilon = 0.01
k = 24.0
guess = k/2.0
index = 0

while abs(guess*guess - k) >= epsilon:
    index += 1
    guess = guess - (((guess**2) - k)/(2*guess))
    print('loop', index)

print('Square root of', k, 'is about', guess)
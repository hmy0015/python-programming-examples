"""
   그림 3.4의 코드에서 세제곱근의 근사값을 구할 때, 음수와 양수 모두를 계산 가능할 수 있도록 수정하시오. (p.39)
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, ', high =', high, ', ans =', ans)
    numGuesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)
"""
    입력 받은 int형 숫자의 root와 pwr를 출력하시오.
    단, pwr는 0과 6 사이이며, root ** pwr은 입력 받은 값과 같아야 하고
    만약 그 값을 구할 수 없다면 이에 대한 메시지를 출력하시오. (p.31)
"""

x = int(input('Enter a positive integer : '))
root = x ** (0.5)
pwr = 0

print('root : ', root)
while 0 <= pwr < 6:
    pwr += 1
    val = 0
    if(root ** pwr == x):
        val = root ** pwr
    else:
        val = '거듭 제곱 값이 입력값과 일치하지 않음'

    print(pwr, '.', root, '**', pwr, ':', val)
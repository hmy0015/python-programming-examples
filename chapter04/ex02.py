"""
    fib를 사용하여 fib(5)를 계산한다면, fib(5)를 계산하는 과정에서 fib(2)의 계산을 몇 번이나 수행해야 하는가?
"""
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i , '=', fib(i))

testFib(5)
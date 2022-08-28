"""
    입력받은 정수 x,y의 제곱과 log2 구하기
"""
import numpy

x = int(input('Enter number x : '))
y = int(input('Enter number y : '))

print('x ** y = ', x**y)
print('log(x) = ', int(numpy.log2(x)))
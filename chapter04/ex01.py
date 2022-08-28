""" 
    두 문자열을 인자로 받아서 만약 두 문자열 중 하나라도 서로 부분문자열(substring)을 포함하고 있다면 True, 그렇지 않다면 False를 반환하는 isIn 함수를 작성하시오.
    [힌트] 파이썬의 내장 연산자인 str의 in을 사용하시오.
"""
def isIn(txt, searchword):
    return print(searchword in txt)

txt = input('enter string: ')
searchword = input('enter searchword: ')

isIn(txt, searchword)
# SWEA 4866
# https://bit.ly/3rn9LdI

import sys
sys.stdin = open('sample.txt', 'r')


def check(code):
    dic = {'}': '{', ')': '('}
    s = []
    for c in code:
        if c == '{' or c == '(':
            s.append(c)
        elif c == '}' or c == ')':
            if s and dic[c] == s[-1]: s.pop()
            else:
                s.append(c)
                break

    return print(f'#{tc} {0 if s else 1}')


for tc in range(1, int(input())+1):
    code = list(input())
    s = []

    check(code)
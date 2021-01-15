# SWEA 5186
# https://bit.ly/35wZQc5

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = float(input())

    res = ''
    for i in range(1, 13):
        if n >= 2 ** (-i):
            res += '1'
            n -= 2 ** (-i)
        else: res += '0'

        if not n:
            print(f'#{tc} {res}')
            break
    else:
        print(f'#{tc} overflow')



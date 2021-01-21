# SWEA 5201
# https://bit.ly/38Xw1U8

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    wi, ti = list(map(int, input().split())), list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort()

    res = 0
    for j in range(n):
        if ti[m-1] >= wi[j]:
            res += wi[j]
            m -= 1

        if not m: break

    print(f'#{tc} {res}')
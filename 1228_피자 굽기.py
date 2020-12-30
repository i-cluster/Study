# SWEA 5099
# https://bit.ly/34NvTUQ

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ci = list(map(int, input().split()))

    piz, nx_piz = list(i for i in range(n)), n

    i, j = -1, n
    while nx_piz != m - 1 + n:
        i = (i+1) % j
        p = piz[i]
        if ci[p] != 1: ci[p] //= 2
        else:
            if nx_piz < m: piz[i] = nx_piz
            else:
                piz.remove(p)
                j -= 1
                i -= 1
            nx_piz += 1

    print(f'#{tc} {piz[0] + 1}')
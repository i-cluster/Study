# SWEA 4837
# https://bit.ly/37iFnJe

import sys
sys.stdin = open('sample.txt', 'r')


def partition(s, p, sp):
    if not p:
        global cnt
        if sp == k:
            cnt += 1
    elif s <= 12:
        if sp + s <= k:
            partition(s+1, p-1, sp + s)
        partition(s+1, p, sp)


for tc in range(1, int(input())+1):
    n, k = map(int, input().split())

    cnt = 0
    partition(1, n, 0)

    print(f'#{tc} {cnt}')
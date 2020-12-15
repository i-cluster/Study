# SWEA 4835
# https://bit.ly/2KrZETA

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ai = list(map(int, input().split()))

    s = sum(ai[:m])
    max_s, min_s = s, s
    for i in range(m, n):
        s += ai[i] - ai[i-m]
        if s > max_s:
            max_s = s
        if s < min_s:
            min_s = s

    print(f'#{tc} {max_s - min_s}')
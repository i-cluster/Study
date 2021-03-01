# SWEA 1206
# https://bit.ly/3b0tdXj

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    ans = 0
    for i in range(2, n-2):
        b, h = building[i], building[i-2:i+3]
        if max(h) == b:
            h.remove(b)
            ans += b - max(h)

    print(f'#{tc} {ans}')
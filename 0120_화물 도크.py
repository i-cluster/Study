# SWEA 5202
# https://bit.ly/38Xw1U8

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    time = [tuple(map(int, input().split())) for _ in range(n)]

    time.sort(key=lambda x: x[1])
    res, tm = 0, 0
    for i in range(n):
        if time[i][0] >= tm:
            res += 1
            tm = time[i][1]

    print(f'#{tc} {res}')
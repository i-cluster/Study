# SWEA 1954
# https://bit.ly/3b0tdXj

d = [0, 1, 0, -1, 0]

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    i, di = 1, 0
    x, y = 0, 0
    while i <= n ** 2:
        arr[x][y] = i
        dx, dy = x + d[di], y + d[di + 1]
        if not 0 <= dx < n or not 0 <= dy < n or arr[dx][dy]:
            di = (di + 1) % 4
        x, y = x + d[di], y + d[di + 1]
        i += 1

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()
# SWEA 5644
# https://bit.ly/2Qzcumk

# 지도 + cp 위치 field, 충전량 btr
# cp 범위 내 사용자 cp1, cp2, ...

d = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    field = [[0] * 10 for _ in range(10)]
    m, a = map(int, input().split())
    moveA, moveB = tuple(map(int, input().split())), tuple(map(int, input().split()))
    for _ in range(a):
        x, y, c, p = map(int, input().split())
        x -= 1; y -= 1
        for i in range(-c, c+1):
            if 0 <= x+i < 10:
                ci = c - abs(i)
                mx, mn = max(y-ci, 0), min(y+ci+1, 10)
                for j in range(mx, mn):
                    if not field[x+i][j]:
                        field[x+i][j] = [p]
                    else:
                        field[x+i][j].append(p)

    posA, posB = [0, 0], [9, 9]
    for k in range(m):
        posA[0] += d[moveA[k]][0]; posA[1] += d[moveA[k]][1]
        posB[0] += d[moveA[k]][0]; posB[1] += d[moveA[k]][1]
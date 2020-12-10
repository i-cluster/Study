# SWEA 5644

import sys
sys.stdin = open('sample.txt', 'r')

d = [-1, 0, 1, 0, -1]

for tc in range(1, int(input())+1):
    m, a = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(2)]

    BC = [[''] * 10 for _ in range(10)]
    pw, on = {}, ['' * a]
    for k in range(a):
        x, y, c, p = map(int, input().split())
        k = str(k)
        pw[k] = p

        x -= 1; y -= 1
        for i in range(-c, c+1):
            for j in range(-c+abs(i), c+1-abs(i)):
                if 0 <= y+j < 10 and 0 <= x+i < 10:
                    BC[y+j][x+i] += k

    a, b = (0, 0, []), (9, 9, [])
    pwa, pwb = 0, 0
    # 이동 전 충전

    # 이동
    for r in range(m):
        ai, bi = (a[0] + d[route[0][r]], a[1] + d[route[0][r]-1], []), (b[0] + d[route[1][r]], b[1] + d[route[1][r]-1], [])
        # 충전 범위 진입
        for i in BC[a[1]][a[0]]:
            on[int(i)] += 'a'

        print(a, b)





'''
1
20 3
2 2 3 2 2 2 2 3 3 4 4 3 2 2 3 3 3 2 2 3
4 4 1 4 4 1 4 4 1 1 1 4 1 4 3 3 3 3 3 3
4 4 1 100
7 10 3 40
6 3 2 70
'''
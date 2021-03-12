# SWEA 1249
# https://bit.ly/3ctoCfE

from collections import deque

d = (0, 1, 0, -1, 0)


def recover():
    que = deque([(0, 0)])
    while que:
        i, j = que.popleft()
        for k in range(4):
            di, dj = i + d[k], j + d[k+1]
            if 0 <= di < n and 0 <= dj < n and v[i][j] + area[di][dj] < v[di][dj]:
                v[di][dj] = v[i][j] + area[di][dj]
                que.append((di, dj))


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    area = [list(map(int, list(input()))) for _ in range(n)]

    v = [[(100 ** 2) * 10] * n for _ in range(n)]
    v[0][0] = 0
    recover()

    print(f'#{tc} {v[-1][-1]}')
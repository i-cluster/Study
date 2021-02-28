# SWEA 1868
# https://bit.ly/3aGQi12

from collections import deque

d = (0, 1, 0, -1, 1, 1, -1, -1, 0)


def mine(i, j):
    que = deque([(i, j)])
    while que:
        x, y = que.popleft()
        if not field[x][y]:
            for k in range(8):
                dx, dy = x + d[k], y + d[k+1]
                if 0 <= dx < n and 0 <= dy < n:
                    que.append((dx, dy))
        field[x][y] = '.'


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    field = [[0] * n for _ in range(n)]

    for i in range(n):
        arr = input()
        for j in range(n):
            if arr[j] == '*':
                field[i][j] = '*'
                for k in range(8):
                    if 0 <= i + d[k] < n and 0 <= j + d[k+1] < n:
                        try: field[i + d[k]][j + d[k+1]] += 1
                        except: pass

    click = 0
    for i in range(n):
        for j in range(n):
            if not field[i][j]:
                mine(i, j)
                click += 1
            elif field[i][j] == '*': field[i][j] = '.'

    print(f'#{tc} {click + (n ** 2) - sum(arr.count(".") for arr in field)}')
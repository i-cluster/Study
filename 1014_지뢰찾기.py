# SWEA 1868

import sys
sys.stdin = open('sample.txt', 'r')

d = [0, 1, -1, 1, 1, 0, -1, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    land = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if land[i][j] == '*':
                for k in range(8):
                    di, dj = i + d[k], j + d[k+1]
                    if 0 <= di < n and 0 <= dj < n:
                        if land[di][dj] == '.': land[di][dj] = 1
                        elif land[di][dj] != '*': land[di][dj] += 1

    op = 0
    for i in range(n):
        for j in range(n):
            if land[i][j] == '.':
                op += 1
                que = [(i, j)]
                while que:
                    x, y = que.pop()
                    land[x][y] = '/'
                    for k in range(8):
                        dx, dy = x + d[k], y + d[k+1]
                        if 0 <= dx < n and 0 <= dy < n and land[dx][dy] == '.':
                            que.append((dx, dy))

            elif type(land[i][j]) == int:
                for k in range(8):
                    di, dj = i + d[k], j + d[k+1]
                    if 0 <= di < n and 0 <= dj < n and (land[di][dj] == '.' or land[di][dj] == '/'):
                        break
                else:
                    op += 1

    print(f'#{tc} {op}')
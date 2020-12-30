# SWEA 5105
# https://bit.ly/2MgsA29

def bfs():
    vi = [list(0 for _ in range(n)) for _ in range(n)]
    vi[que[0][0]][que[0][1]] = 1

    while que:
        x, y = que.pop(0)
        for k in range(4):
            dx, dy = x + d[k], y + d[k+1]
            if 0 <= dx < n and 0 <= dy < n and not vi[dx][dy]:
                if maze[dx][dy] == '3': return vi[x][y] -1
                if maze[dx][dy] == '0':
                    que.append((dx, dy))
                    vi[dx][dy] = vi[x][y] + 1
    return 0


d = [0, 1, 0, -1, 0]

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    maze, que = [], []
    for _ in range(n):
        maze.append(input())
        if '2' in maze[-1]:
            que.append((len(maze) - 1, maze[-1].index('2')))

    print(f'#{tc} {bfs()}')
# SWEA 4875
# https://bit.ly/3rz3ZFC

def dfs():
    vi = [list(0 for _ in range(n)) for _ in range(n)]
    vi[st[0][0]][st[0][1]] = 1

    while st:
        x, y = st.pop(0)
        for k in range(4):
            dx, dy = x + d[k], y + d[k+1]
            if 0 <= dx < n and 0 <= dy < n:
                if maze[dx][dy] == '3': return 1
                if maze[dx][dy] == '0' and not vi[dx][dy]:
                    vi[dx][dy] = 1
                    st.append((dx, dy))
    return 0


import sys
sys.stdin = open('sample.txt', 'r')

d = [0, 1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    maze, st = [], []
    for _ in range(n):
        maze.append(input())
        if '2' in maze[-1]:
            st.append((len(maze) - 1, maze[-1].index('2')))

    print(f'#{tc} {dfs()}')
# SWEA 1227

for tc in range(1, 11):
    n = int(input())
    maze, que = [], []

    for _ in range(100):
        arr = input()
        maze.append(arr)
        if '2' in arr:
            que.append((arr.index('2'), len(maze) - 1))

    v = [[0] * 100 for _ in range(100)]
    d = [0, -1, 0, 1, 0]

    res = 1
    while que:
        x, y = que.pop(0)
        if maze[y][x] == '3': break
        v[y][x] = 1
        for i in range(4):
            dx, dy = x + d[i], y + d[i + 1]
            if maze[dy][dx] != '1' and not v[dy][dx]:
                que.append((dx, dy))
    else: res = 0

    print(f'#{n} {res}')
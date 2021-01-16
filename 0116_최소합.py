# SWEA 5188
# https://bit.ly/3ielHKz

def min_sum(x, y):
    global min_s
    if x == y == n-1:
        min_s = vi[x][y]
    else:
        for k in range(2):
            dx, dy = x + d[k], y + d[k+1]
            if 0 <= dx < n and 0 <= dy < n and not vi[dx][dy] and vi[x][y] + arr[dx][dy] < min_s:
                vi[dx][dy] = vi[x][y] + arr[dx][dy]
                min_sum(dx, dy)
                vi[dx][dy] = 0


import sys
sys.stdin = open('sample.txt', 'r')

d = [0, 1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    vi = [[0] * n for _ in range(n)]
    vi[0][0] = arr[0][0]
    min_s = (n ** 2) * 10
    min_sum(0, 0)

    print(f'#{tc} {min_s}')
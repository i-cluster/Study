# JO 1707

n = int(input())
arr = [list(0 for _ in range(n)) for _ in range(n)]

d = [0, 1, 0, -1, 0]
x, y, k = 0, 0, 0
for i in range(1, n ** 2 + 1):
    arr[x][y] = i
    dx, dy = x + d[k], y + d[k+1]
    if not 0 <= dx < n or not 0 <= dy < n or arr[dx][dy]:
        k = (k + 1) % 4
    x, y = x + d[k], y + d[k+1]

for ar in arr:
    for a in ar:
        print(a, end=' ')
    print()
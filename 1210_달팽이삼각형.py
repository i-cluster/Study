# JO 1337

n = int(input())
D = [(1, 1), (0, -1), (-1, 0)]
arr = [list(0 for _ in range(k)) for k in range(1, n+1)]

m, d, i = n, 0, 0
x, y = -1, -1
while m:
    x, y = x + D[d][0], y + D[d][1]
    arr[x][y] = i
    i = (i + 1) % 10
    m -= 1

    if not m:
        n -= 1
        m = n
        d = (d + 1) % 3

for ar in arr:
    for a in ar:
        print(a, end=' ')
    print()
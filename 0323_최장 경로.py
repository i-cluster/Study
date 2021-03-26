# SWEA 2814
# https://bit.ly/2NIh5Bp

def routing(s, c):
    global max_routes
    v[s] = 1

    for e in nodes[s]:
        if not v[e]:
            routing(e, c+1)
            v[e] = 0

    if c > max_routes:
        max_routes = c


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    nodes = {i: [] for i in range(1, n+1)}
    for _ in range(m):
        x, y = map(int, input().split())
        nodes[x].append(y)
        nodes[y].append(x)

    max_routes = 0
    for k in range(1, n+1):
        v = [0] * (n+1)
        routing(k, 1)

    print(f'#{tc} {max_routes}')
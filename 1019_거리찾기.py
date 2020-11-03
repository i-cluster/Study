# https://www.acmicpc.net/problem/18352
# BOJ 18352

from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
road = {i: [] for i in range(n+1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    road[a].append(b)

V = [0] * (n + 1)
Q, q = deque([x]), deque([])
V[x] = 1
while Q:
    s = Q.popleft()
    for i in road[s]:
        if not V[i]:
            q.append(i)
            V[i] = 1

    if not Q:
        k -= 1
        if not k: break
        Q.extend(q)
        q = deque([])

if not q:
    print(-1)
else:
    q = sorted(q)
    for i in q:
        print(i)
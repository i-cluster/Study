# SWEA 5102
# https://bit.ly/3o1Jak5

def bfs(s, g):
    vi, que = list(0 for _ in range(v+1)), [s]
    vi[s] = 1

    while que:
        s = que.pop(0)
        for k in node[s]:
            if k == g: return vi[s]
            if not vi[k]:
                que.append(k)
                vi[k] = vi[s] + 1
    return 0


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    v, e = map(int, input().split())

    node = {i: [] for i in range(1, v+1)}
    for _ in range(e):
        i, j = map(int, input().split())
        node[i].append(j)
        node[j].append(i)

    s, g = map(int, input().split())

    print(f'#{tc} {bfs(s, g)}')
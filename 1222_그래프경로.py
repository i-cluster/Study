# SWEA 4871
# https://bit.ly/38jXTjC

import sys
sys.stdin = open('sample.txt', 'r')


def dfs(s, g):
    stk, vi = [s], [0] * (v + 1)
    vi[s] = 1
    while stk:
        s = stk.pop(0)
        if nd.get(s):
            for k in nd[s]:
                if k == g: return 1
                if not vi[k]:
                    stk.append(k)
                    vi[k] = 1
    else: return 0


for tc in range(1, int(input())+1):
    v, e = map(int, input().split())
    nd = {}

    for _ in range(e):
        i, j = map(int, input().split())
        if i in nd.keys():
            nd[i].append(j)
        else:
            nd[i] = [j]

    s, g = map(int, input().split())

    print(f'#{tc} {dfs(s, g)}')
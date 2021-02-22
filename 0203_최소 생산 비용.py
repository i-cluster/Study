# SWEA 5209
# https://bit.ly/3sRAT5b

def minimize(k, cost):
    global min_cost
    if k == n:
        if min_cost > cost: min_cost = cost
    else:
        for i in range(n):
            if not u[i] and cost + costs[k][i] <= min_cost:
                u[i] = 1
                minimize(k+1, cost + costs[k][i])
                u[i] = 0


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]

    min_cost, u = 99 * (n ** 2), [0] * n
    minimize(0, 0)

    print(f'#{tc} {min_cost}')
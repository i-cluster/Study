# SWEA 4881
# https://bit.ly/3rx8O2e

def minimize(i, s):
    if i == n:
        global min_s
        if s < min_s: min_s = s
    else:
        for j in range(n):
            if not u[j] and s + arr[i][j] < min_s:
                u[j] = 1
                minimize(i+1, s + arr[i][j])
                u[j] = 0

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    u = [0] * n
    min_s = 10 * (n ** n)
    minimize(0, 0)

    print(f'#{tc} {min_s}')
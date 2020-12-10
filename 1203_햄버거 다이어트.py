# SWEA 5215

import sys
sys.stdin = open('sample.txt', 'r')

from copy import deepcopy

for tc in range(1, int(input())+1):
    n, l = map(int, input().split())
    ing = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [list(0 for i in range(l+1)) for _ in range(2)]

    for i in range(n):
        t, k = ing[i][0], ing[i][1]
        dp[0] = deepcopy(dp[1])
        for j in range(1, l+1):
            if j >= k:
                dp[1][j] = max(dp[0][j], dp[0][j-k] + t)
            else:
                dp[1][j] = dp[0][j]

    print(f'#{tc} {dp[1][-1]}')
# SWEA 2115

from copy import deepcopy

import sys
sys.stdin = open('sample.txt', 'r')


# 꿀 캐기
def catch(x, y, p, t):
    if p < 2:
        # for i in range(x, n):
        while x < n:
            # for j in range(n-m+1):
            while y < n-m+1:
                # DP
                dp = [list(0 for _ in range(c+1)) for _ in range(2)]
                for k in honey[x][y:y+m]:
                    dp[0] = deepcopy(dp[1])
                    for b in range(1, c+1):
                        if b >= k:
                            dp[1][b] = max(dp[0][b-k] + k ** 2, dp[0][b])
                        else:
                            dp[1][b] = dp[0][b]
                h = dp[1][-1]
                if t+h > max_h[p]:
                    max_h[p] = t+h
                    catch(x, y+m+1, p+1, t+h)
                y += 1

            x += 1
            y = 0


for tc in range(1, int(input())+1):
    # 벌통 크기 n, 선택 수 m, 최대 수량 c
    n, m, c = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(n)]

    max_h = [0, 0]
    catch(0, 0, 0, 0)

    print(f'#{tc} {max_h}')
# SWEA 2806
# https://bit.ly/391iMSa

def location(k, s, d, loc):
    global cnt
    if not k: cnt += 1
    else:
        i, j = loc[0], loc[1]
        while i < n:
            while j < n:
                if not xy[0][i] and not xy[1][j] and i + j not in s and i - j not in d:
                    xy[0][i], xy[1][j] = 1, 1
                    location(k - 1, s + [i + j], d + [i - j], (i, j))
                    xy[0][i], xy[1][j] = 0, 0
                j += 1
            i += 1; j = 0


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())

    cnt = 0
    xy = [list(0 for i in range(n)) for _ in range(2)]
    location(n, [], [], (0, 0))

    print(f'#{tc} {cnt}')
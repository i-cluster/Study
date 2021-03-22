# SWEA 2806
# https://bit.ly/391iMSa

def location(k, s, d):
    global cnt
    if not k: cnt += 1
    else:
        for i in range(n):
            for j in range(n):
                if not xy[0][i] and not xy[1][j] and i + j not in s and i - j not in d:
                    xy[0][i], xy[1][j] = 1, 1
                    location(k - 1, s + [i + j], d + [i - j])
                    xy[0][i], xy[1][j] = 0, 0


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())

    cnt = 0
    xy = [list(0 for i in range(n)) for _ in range(2)]
    location(n, [], [])

    print(f'#{tc} {cnt}')
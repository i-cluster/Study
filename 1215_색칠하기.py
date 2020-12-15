# SWEA 4836
# https://bit.ly/3gLwNGa

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    block = [list(0 for _ in range(10)) for _ in range(10)]
    mix = 0

    for _ in range(n):
        r1, c1, r2, c2, cl = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                block[i][j] += cl
                if block[i][j] == 3:
                    mix += 1

    print(f'#{tc} {mix}')
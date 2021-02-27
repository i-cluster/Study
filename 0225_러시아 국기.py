# SWEA 4613
# https://bit.ly/3aGQi12

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    color = []

    for _ in range(n):
        arr = input()
        color.append(list(map(lambda x: m - x, (arr.count('W'), arr.count('B'), arr.count('R')))))

    paint = list(zip(*color))

    min_paint = n * m
    for i in range(1, n-1):
        for j in range(i+1, n):
            s = sum(paint[0][:i]) + sum(paint[1][i:j]) + sum(paint[2][j:])
            if s < min_paint: min_paint = s

    print(f'#{tc} {min_paint}')
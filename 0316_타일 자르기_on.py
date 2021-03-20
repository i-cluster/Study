# SWEA 1812
# https://bit.ly/3cz59uo

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    tile = list(map(int, input().split()))
    tile.sort()

    print(f'#{tc}')
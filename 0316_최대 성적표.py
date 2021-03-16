# SWEA 4466
# https://bit.ly/3ljkS4G

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))

    print(f'#{tc} {sum(sorted(score, reverse=True)[:k])}')
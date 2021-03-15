# SWEA 1204
# https://bit.ly/3tjboJo

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, score = input(), list(map(int, input().split()))

    sc = [0] * 101
    for k in range(1000):
        sc[100 - score[k]] += 1

    print(f'#{tc} {100 - sc.index(max(sc))}')
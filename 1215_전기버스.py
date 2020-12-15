# SWEA 4831
# https://bit.ly/387lXpN

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    # 최대 충전량 k, 종점 n, 충전기 m
    k, n, m = map(int, input().split())
    crg = [0] + list(map(int, input().split())) + [n]

    btr, cnt = k, 0
    for i in range(1, m+1):
        btr -= crg[i] - crg[i-1]
        if crg[i+1] > crg[i] + btr:
            btr = k
            cnt += 1
        if crg[i] + btr < crg[i+1]:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
# SWEA 1204
# https://bit.ly/3b0tdXj

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = input()
    score = list(map(int, input().split()))
    count = [0] * 101

    for i in range(1000):
        count[100 - score[i]] += 1

    print(f'#{tc} {100 - count.index(max(count))}')
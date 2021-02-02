# SWEA 5208
# https://bit.ly/3sRAT5b

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    crg = list(map(int, input().split()))

    cnt = 0
    idx, btr = 1, crg[1]
    while idx + btr < crg[0]:
        li = list(i+crg[idx+i] for i in range(1, btr+1))
        idx += li.index(max(li)) + 1
        btr = crg[idx]
        cnt += 1

    print(f'#{tc} {cnt}')
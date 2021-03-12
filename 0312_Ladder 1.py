# SWEA 1210
# https://bit.ly/3ctoCfE

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, 11):
    n = input()
    ladder = [list(input().split()) for _ in range(100)]
    i, j = 99, ladder[99].index('2')

    while i:
        for k in (-1, 1):
            if 0 <= j+k <= 99 and ladder[i][j+k] == '1':
                while 0 <= j+k <= 99 and ladder[i][j+k] != '0':
                    j += k
                break
        i -= 1

    print(f'#{tc} {j}')
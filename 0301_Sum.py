# SWEA 1209
# https://bit.ly/3b0tdXj

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    diag_sum, diag_sum_rev = 0, 0
    for i in range(100):
        row_sum, col_sum= 0, 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if row_sum > max_sum: max_sum = row_sum
        if col_sum > max_sum: max_sum = col_sum
        diag_sum += arr[i][i]
        diag_sum_rev += arr[i][99 - i]

    print(f'#{tc} {max(max_sum, diag_sum, diag_sum_rev)}')
# SWEA 4861
# https://bit.ly/3mEkUTM

import sys
sys.stdin = open('sample.txt', 'r')


def pal(n, m):
    for i in range(n):
        for j in range(n-m+1):
            for k in range(m // 2):
                if arr[i][j+k] != arr[i][j+m-1-k]: break
            else:
                return arr[i][j:j+m]

            for k in range(m // 2):
                if arr[j+k][i] != arr[j+m-1-k][i]: break
            else:
                return ''.join(arr[j+k][i] for k in range(m))


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(input() for _ in range(n))

    print(f'#{tc} {pal(n, m)}')
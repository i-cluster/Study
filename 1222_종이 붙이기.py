# SWEA 4869
# https://bit.ly/3rkj0LF

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())

    arr = [1, 3]
    for _ in range(n//10 - 2):
        arr.append(arr[-2] * 2 + arr[-1])

    print(f'#{tc} {arr[-1]}')
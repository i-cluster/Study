# SWEA 2805
# https://bit.ly/2PberEH

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    field = [list(map(int, list(input()))) for _ in range(n)]

    print(f'#{tc} {sum(sum(field[i][abs(n//2 - i):n - abs(n//2 - i)]) for i in range(n))}')
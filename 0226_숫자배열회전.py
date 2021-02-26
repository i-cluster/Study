# SWEA 1961
# https://bit.ly/3aGQi12

def turn(k, ar):
    for i in range(n):
        for j in range(n-1, -1, -1):
            turned[i][k] += ar[j][i]
    return list(turned[i][k] for i in range(n))


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(input().split()) for _ in range(n)]

    turned = [[''] * 3 for _ in range(n)]
    for k in range(3):
        arr = turn(k, arr)

    print(f'#{tc}')
    for i in range(n):
        for j in range(3):
            print(turned[i][j], end=' ')
        print()
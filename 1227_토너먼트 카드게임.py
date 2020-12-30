# SWEA 4880
# https://bit.ly/3hlyiLj

def table(i, j):
    if i == j:
        return i
    else:
        a = table(i, (i+j) // 2)
        b = table((i+j) // 2 + 1, j)
        return b if (cards[a], cards[b]) in [(3, 1), (1, 2), (2, 3)] else a


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    cards = list(map(int, input().split()))

    print(f'#{tc} {table(0, n-1) + 1}')
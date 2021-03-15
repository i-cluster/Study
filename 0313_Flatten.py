# SWEA 1208
# https://bit.ly/3cGWPc7

def dump(n, k, p):
    while n:
        while box[k] == box[k+p]:
            k += p

        fl = (box[k+p] - box[k]) * k
        if fl < n:
            n -= fl
            k += p
        else:
            return box[k] + p * (n // (k * p))


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    box = [0] + list(map(int, input().split()))
    box.sort()

    print(f'#{tc} {dump(n, -1, -1) - dump(n, 1, 1)}')
# SWEA 4013
# https://bit.ly/38xRLpa

def spin(n, d):
    v[n] = 1
    if n < 4 and not v[n + 1] and magnet[n][key[n] - 6] != magnet[n + 1][key[n + 1] - 2]:
        spin(n + 1, -d)
    if n >= 2 and not v[n - 1] and magnet[n][key[n] - 2] != magnet[n - 1][key[n - 1] - 6]:
        spin(n - 1, -d)

    key[n] = (key[n] + (-1) * d) % 8


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input()) + 1):
    k = int(input())
    magnet = [''] + [list(map(int, input().split())) for _ in range(4)]
    key = [0] * 5

    for _ in range(k):
        n, d = map(int, input().split())
        v = [0] * 5
        spin(n, d)

    score = 0
    for i in range(1, 5):
        if magnet[i][key[i]]:
            score += 2 ** (i - 1)

    print(f'#{tc} {score}')
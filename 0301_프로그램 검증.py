# SWEA 1824
# https://bit.ly/3b0tdXj

cons = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}


def random(i, j):
    for di, dj in cons.values():
        if not arr[(i + di) // r][(j + dj) // c]:
            return di, dj

    return 0, 1


def run():
    i, j, m, d = 0, 0, 0, (0, 1)
    while arr[i][j] != '@':

        a = arr[i][j]
        if a in cons.keys(): d = cons[a]
        elif a in ('+', '-'): m += 1 if a == '+' else -1
        elif a in ('_', '|'):
            if a == '_': d = cons['<'] if m else cons['>']
            else: d = cons['^'] if m else cons['v']
        elif a == '?': d = random(i, j)
        elif a != '.': m = int(a)

        v[i][j] = 1
        i = (i + d[0]) // r
        j = (j + d[1]) // c

    return 'YES'


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    r, c = map(int, input().split())
    arr = list(input() for _ in range(r))

    v = [[0] * c for _ in range(r)]

    print(f'#{tc} {run()}')
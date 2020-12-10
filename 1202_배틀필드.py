# SWEA 1873

import sys
sys.stdin = open('sample.txt', 'r')


def shoot(dt, x, y):
    while 0 <= x + dt[1][0] < h and 0 <= y + dt[1][1] < w:
        x, y = x + dt[1][0], y + dt[1][1]
        if field[x][y] == '*':
            field[x][y] = '.'
            break
        elif field[x][y] == '#':
            break


def move(i, x, y):
    global dt
    dt = d[i]
    dx, dy = x + dt[1][0], y + dt[1][1]
    if 0 <= dx < h and 0 <= dy < w and field[dx][dy] == '.':
        x = dx; y = dy
    return (x, y)


d = {'U': ('^', (-1, 0)), 'D': ('v', (1, 0)), 'L': ('<', (0, -1)), 'R': ('>', (0, 1))}

for tc in range(1, int(input())+1):
    h, w = map(int, input().split())
    field, dt = [], ''
    for _ in range(h):
        arr = list(input())
        field.append(arr)
        if not dt:
            for a in arr:
                if a not in ['.', '*', '#', '-']:
                    x, y = len(field) - 1, arr.index(a)
                    for v in d.values():
                        if a in v: dt = v
                    field[x][y] = '.'
                    break

    n, acts = input(), input()

    for a in acts:
        if a == 'S':
            shoot(dt, x, y)
        else:
            x, y = move(a, x, y)

    field[x][y] = dt[0]

    print(f'#{tc} ', end='')
    for f in field:
        print(''.join(f))
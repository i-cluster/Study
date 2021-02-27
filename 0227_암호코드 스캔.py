# SWEA 1242
# https://bit.ly/3aGQi12

decode = {'3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4', '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'}


def ratio(arr, i, x):
    r = str(i)
    while i:
        if arr[i] != arr[i+1]:
            r += str((i + 1 - int(r[-1])) // x)
            if len(r) == 4:
                return r[1:] + str(7 - sum(list(map(int, r[1:]))))
        i += 1


def test(arr, j):
    x = 1
    while x:
        if ratio(arr, j - (7 * x), x) in decode.keys(): break
        x += 1

    code, num = '', 0
    for k in range(8):
        p = decode[ratio(arr, j - (7 * x), x)]
        code = code + p
        num += int(p) * 3 if k % 2 else int(p)
        j -= 7 * x

    return sum(int(c) for c in code) if not num % 10 else 0


def scan():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if data[i][j] == '1':
                test(data[i], j+1)


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    data = list(input() for _ in range(n))

    print()
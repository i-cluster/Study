# SWEA 1961
# https://bit.ly/3aGQi12

decode = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}


def test(arr, j):
    code, num = '', 0
    for k in range(8):
        p = decode[arr[j-7:j]]
        code = code + p
        num += int(p) * 3 if k % 2 else int(p)
        j -= 7

    return sum(int(c) for c in code) if not num % 10 else 0


def scan():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            if data[i][j] == '1':
                return test(data[i], j+1)


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    data = list(input() for _ in range(n))

    print(f'#{tc} {scan()}')
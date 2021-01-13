# SWEA 5185
# https://bit.ly/35wZQc5

def bin_func(i):
    bi = ''
    for j in range(3, -1, -1):
        if i & (1 << j): bi += '1'
        else: bi += '0'

    return bi


dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, st = input().split()
    res = ''

    for s in st:
        if s in dic.keys(): res += bin_func(dic[s])
        else: res += bin_func(int(s))

    print(f'{tc} {res}')
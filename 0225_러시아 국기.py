# SWEA 4615
# https://bit.ly/3aGQi12

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    words = []

    for _ in range(n):
        arr = input()
        words.append(tuple(map(lambda x: m - x, (arr.count('W'), arr.count('B'), arr.count('R')))))

    

    print(f'#{tc} {words}')
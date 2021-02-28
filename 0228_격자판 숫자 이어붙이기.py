# SWEA 2819
# https://bit.ly/3aGQi12

d = [0, 1, 0, -1, 0]


def number(n, num, i, j):
    if n == 6:
        if num not in nums: nums.append(num)
    else:
        for k in range(4):
            di, dj = i + d[k], j + d[k+1]
            if 0 <= di < 4 and 0 <= dj < 4:
                number(n+1, num + board[di][dj], di, dj)


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    board = [list(input().split()) for _ in range(4)]

    nums = []
    for i in range(4):
        for j in range(4):
            number(0, board[i][j], i, j)

    print(f'#{tc} {len(nums)}')
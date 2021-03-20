# SWEA 5658
# https://bit.ly/3s4NlOh

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    hex_str = input() * 2

    l, nums = n//4, []
    for i in range(l):
        for p in range(4):
            pw = hex_str[p * l + i:(p + 1) * l + i]
            if pw not in nums: nums.append(pw)

    print(f'#{tc} {int("0x" + sorted(nums, reverse=True)[k-1], 16)}')
# SWEA 5658
# https://bit.ly/3s4NlOh

dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(int(input())+1):
    n, k = map(int, input().split())
    hex_str = input() * 2

    l, nums = len(hex_str)//8, []
    for i in range(l):
        for p in range(4):
            s = hex_str[i+(p*l):i+(p+1)*l]
            pw = 0
            for j in range(l):
                pw += s[j] * (16 ** j)
            if pw not in nums: nums.append(pw)

    print(f'#{tc} {sorted(nums)[k]}')
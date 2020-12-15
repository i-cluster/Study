# SWEA 4834
# https://bit.ly/2KoFdqM

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(input())

    cnt = [0] * 10
    for num in nums:
        cnt[int(num)] += 1

    max_num, max_c = '', 0
    for i in range(10):
        if cnt[i] >= max_c:
            max_num, max_c = i, cnt[i]

    print(f'#{tc} {max_num} {max_c}')
# SWEA 4843
# https://bit.ly/3gLQXji

import sys
sys.stdin = open('sample.txt', 'r')


def partition(l, h):
    pv = nums[l]
    i, j = l-1, h+1

    while True:
        i += 1
        while nums[i] < pv: i += 1

        j -= 1
        while nums[j] > pv: j -= 1

        if i >= j: return j
        nums[i], nums[j] = nums[j], nums[i]


def qsort(l, h):
    if l < h:
        pi = partition(l, h)

        qsort(l, pi)
        qsort(pi + 1, h)


for tc in range(1, int(input())+1):
    n = int(input())
    nums = list(map(int, input().split()))

    qsort(0, n-1)

    print(f'#{tc} ', end='')
    for i in range(5):
        print(nums[-i-1], nums[i], end=' ')
    print()
# SWEA 1824
# https://bit.ly/3b0tdXj

def change(nums, c):
    i = 0
    while c:
        m = max(nums[i:])
        cnt = nums.count(m)

        arr = nums[i:i+m]
        for j in range(cnt):
            a, k = arr.index(max(arr[j:])), nums.index(m, j)
            nums[a], nums[k] = nums[k], nums[a]
            c -= 1
            if not c: return

        i += cnt


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    nums, c = input().split()
    nums, c = list(map(int, nums)), int(c)

    change(nums, c)

    print(f'#{tc}')
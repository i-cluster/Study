# SWEA 1824
# https://bit.ly/3b0tdXj

def change(nums, c, l):
    i = 0
    while c:
        m = max(nums[i:])
        n = nums.count(m)

        v = []
        while n:
            if nums[i] < m:
                v.append((i, nums[i]))
            n -= 1

        j = i + 1
        v.sort(key= lambda x: x[1])
        while v:
            while nums[j] != m:
                j += 1
            k = v.pop()[0]
            nums[k], nums[j] = nums[j], nums[k]
            j += 1


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    nums, c = input().split()
    nums, c = list(map(int, nums)), int(c)

    change(nums, c, len(nums))

    print(f'#{tc} {nums}')
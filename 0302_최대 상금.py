# SWEA 1244
# https://bit.ly/3b0tdXj

def change(nums, c, l):
    i, m_cnt = 0, 0
    while c and i < l:
        m = max(nums[i:])
        n = nums.count(m)
        if n > m_cnt: m_cnt = n

        v = []
        for _ in range(n):
            if nums[i] < m:
                v.append((i, nums[i]))
                c -= 1
            i += 1
            if not c: break

        j = l
        v.sort(key= lambda x: x[1], reverse=True)
        while v:
            while nums[j] != m:
                j -= 1
            k = v.pop()[0]
            nums[k], nums[j] = nums[j], nums[k]
            j -= 1

    if c % 2 and m_cnt == 1: nums[-2], nums[-1] = nums[-1], nums[-2]


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    nums, c = input().split()
    nums = list(nums)

    change(nums, int(c), len(nums) - 1)

    print(f'#{tc} {"".join(nums)}')
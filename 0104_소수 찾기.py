# PROS 완전탐색 42839
# https://bit.ly/356x4ig

def perm(i, n, nums, cd):
    if i == n-1:
        num = int(''.join(nums[::-1]))
        if num >= 2 and num not in cd:
            s, e = 2, num / 2
            while s <= e:
                if not num % s: break
                else: s += 1
            else:
                cd.append(num)
    else:
        for j in range(i, n):
            nums[i], nums[j] = nums[j], nums[i]
            if int(nums[0]) % 2:
                perm(i+1, n, nums, cd)
            nums[i], nums[j] = nums[j], nums[i]


def decimal(i, n, nums, numbers, cd):
    if i == n:
        perm(0, len(nums), nums, cd)
    else:
        decimal(i+1, n, nums + [numbers[i]], numbers, cd)
        decimal(i+1, n, nums, numbers, cd)


def solution(numbers):
    cd = []
    decimal(0, len(numbers), [], numbers, cd)
    return len(cd)
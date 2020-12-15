# JO 3517
# https://bit.ly/2W9PWIb

N = int(input())
nums = list(map(int, input().split()))
Q = int(input())
bi = list(map(int, input().split()))

for b in bi:
    l, h = 0, N-1
    while l <= h:
        mid = (h + l) // 2
        if nums[mid] == b:
            print(mid, end=' ')
            break
        if nums[mid] < b:
            l = mid + 1
        else:
            h = mid - 1
    else:
        print(-1, end=' ')

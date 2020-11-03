# https://www.acmicpc.net/problem/2309

def who_is_lier(sh, k):
    if k == 2:
        if sh == 100: return 1
    else:
        for i in range(len(height)):
            h = height.pop(i)
            if who_is_lier(sh-h, k+1): return 1
            height.insert(i, h)


height = [int(input()) for _ in range(9)]
sum_height = sum(height)
who_is_lier(sum_height, 0)
height.sort()

for i in height:
    print(i)
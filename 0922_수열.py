# https://www.acmicpc.net/problem/2491

n = int(input())
arr = [-1] + list(map(int, input().split())) + [-1]

cnt, rev_cnt, max_cnt = 0, 0, 0
for i in range(n+1):
    if arr[i] <= arr[i+1]:
        cnt += 1
    else:
        if cnt > max_cnt: max_cnt = cnt
        cnt = 1

    if arr[n-i] >= arr[n+1-i]:
        rev_cnt += 1
    else:
        if rev_cnt > max_cnt: max_cnt = rev_cnt
        rev_cnt = 1

print(max_cnt)
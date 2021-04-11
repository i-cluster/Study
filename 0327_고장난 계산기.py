# SWEA 1808
# https://bit.ly/3sukHWM

# 매회 연산 : '수' + '숫자' / 수 * 숫자
# 연산한 수는 탐색 표에서 이미 나온 적 있는지 확인
# 처음 나온 수라면 탐색 표에 연산 수를 기록(곱셈이면 +2)
# 목표 수를 찾으면 현재 카운트 + 1을 반환

from collections import deque


def cal(arr):
    for a in arr:
        dp[a] = 1

    # 배열 수에 대한 연산
    while arr:
        print(arr)
        a = arr.popleft()
        for num in nums:
            # '수' + '숫자' i, 수 * 숫자 j
            i, j = a * 10 + num, a * num
            for r in (i, j):
                # 목표 수를 찾으면 결과값 반환(연산 버튼 +1)
                if r == n: return dp[a] + 2 if r == i else dp[a] + 3
                # 100만 이하이고 처음 나온 수라면
                if 1 <= r <= 1000000 and not dp[r]:
                    # 숫자 붙이기면 +1, 덧셈이면 +2
                    if r == i: dp[r] = dp[a] + 1
                    else: dp[r] = dp[a] + 2
                    arr.append(r)

    return -1


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    arr = list(input().split())
    # 숫자 버튼 nums, 목표 n
    nums, n = list(i for i in range(10) if arr[i] == '1'), int(input())

    # 탐색 표 + 연산 수 기록
    dp = [0] * (10 ** 6 + 1)

    print(f'#{tc} {cal(deque(nums))}')
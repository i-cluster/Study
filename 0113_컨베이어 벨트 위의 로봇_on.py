# BOJ 20055
# https://www.acmicpc.net/problem/20055

import sys
sys.stdin = open('sample.txt', 'r')

for _ in range(4):
    n, k = map(int, input().split())
    belt = list(map(lambda x: [0, int(x)], sys.stdin.readline().split()))
    n = 2 * n

    rb, move = [], [0] * n
    cnt, i = 0, 0
    while cnt < k:
        # 벨트 이동
        i = (i-1+n)//n
        # 로봇 이동
        for j in range(len(rb)):
            if rb[j]+1 == n: pass
            else:
                if move[rb[j]+1]:
                    rb[j] += 1
                    belt[rb[j]] -= 1
                else: pass
        # 로봇 올리기
        if belt[i] and rb:
            rb.append(i)
            belt[i] -= 1

    print(belt)
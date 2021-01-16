# SWEA 5189
# https://bit.ly/3ielHKz

def cart(s, k, eng):
    global min_eng
    if k == n-1:
        if min_eng > eng + btr[s][0]: min_eng = eng + btr[s][0]
    else:
        for i in range(1, n):
            if i != s and i not in vi and min_eng > eng + btr[s][i]:
                vi.append(i)
                cart(i, k+1, eng + btr[s][i])
                vi.pop()


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    btr = [list(map(int, input().split())) for _ in range(n)]

    vi = []
    min_eng = (n ** 2) * 100
    cart(0, 0, 0)

    print(f'#{tc} {min_eng}')
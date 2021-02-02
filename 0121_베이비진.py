# SWEA 5203
# https://bit.ly/38Xw1U8

def baby_gin(k):
    for i in range(10):
        if k[i] == 3: return 1
        if i < 8 and k[i] and k[i+1] and k[i+2]: return 1

    return 0


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))

    print(f'#{tc} ', end='')
    cs = [[0] * 10, [0] * 10]
    for i in range(12):
        cs[i%2][cards[i]] += 1
        if i >= 4:
            if baby_gin(cs[i%2]): print(i%2+1); break
    else: print(0)
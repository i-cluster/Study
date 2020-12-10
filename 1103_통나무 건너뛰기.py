import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    L = list(map(int, sys.stdin.readline().split()))
    L.sort()

    res = max(L[1] - L[0], L[-1] - L[-2])
    for i in range(n-2):
        dif = L[i+2] - L[i]
        res = max(dif, res)

    print(res)
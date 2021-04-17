# BOJ 3460
# https://www.acmicpc.net/problem/3460

for tc in range(1, int(input())+1):
    n = bin(int(input()))
    l = len(n)

    for k in list((l-1)-i for i in range(l-1, 1, -1) if n[i] == '1'):
        print(k, end=' ')
    print()
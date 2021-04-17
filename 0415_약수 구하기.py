# BOJ 2501
# https://www.acmicpc.net/problem/2501

from sys import stdin
n, k = map(int, stdin.readline().split())

i, j = 1, n+1
factor = []
while i < j:
    if n % i == 0:
        factor.extend([i, n // i])
        j = n // i
    i += 1

print(sorted(set(factor))[k-1] if k <= len(factor) else 0)
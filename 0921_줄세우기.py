# https://www.acmicpc.net/problem/2605

n = int(input())
ticket = [0] + list(map(int, input().split()))

line = ['1']
for i in range(2, n+1):
    line.insert(i-ticket[i]-1, str(i))

print(' '.join(line))
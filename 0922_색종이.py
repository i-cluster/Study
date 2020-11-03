# https://www.acmicpc.net/problem/2563

n = int(input())
paper = [[0] * 100 for _ in range(100)]

color = 0
for _ in range(n):
    i, j = map(int, input().split())

    for k in range(10):
        color += 10 - sum(paper[99-j-k][i:i+10])
        paper[99-j-k][i:i+10] = [1] * 10

print(color)
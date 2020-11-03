# https://www.acmicpc.net/problem/17220
# BOJ 17220
# BFS
# 검거 조건 주의하기

n, m = map(int, input().split())
link = dict()

for _ in range(m):
    p, q = input().split()
    if p not in link.keys(): link[p] = [0, [], []]
    if q not in link.keys(): link[q] = [0, [], []]

    link[q][2].append(p)
    link[p][1].append(q)

Q = list(input().split())
Q.pop(0)
while Q:
    s = Q.pop(0)
    link[s][0] = 1
    for k in link[s][1]:
        for l in link[k][2]:
            if not link[l][0]:
                break
        else:
            Q.append(k)

cnt = 0
for i in link:
    if not link[i][0] and link[i][2]:
        cnt += 1

print(cnt)
# https://www.acmicpc.net/problem/2564

# 가로 r, 세로 c, 전체 둘레 a
r, c = map(int, input().split())
a = 2 * (r+c)
n = int(input())

# (0,0)에서 각 지점까지의 거리
spot = []
for _ in range(n+1):
    d, l = map(int, input().split())

    if d % 2: spot.append((d, l))           # 북,서 지점이면 l
    elif d == 2: spot.append((d,c+l))       # 남쪽 지점이면 l+c
    else: spot.append((d, r+l))             # 동쪽 지점이면 l+r

# 총 이동 거리
patrol = 0
s, k = spot.pop()
for p in spot:
    d, l = p

    if d + s == 5 or d == s:            # (0,0)에서 이동 방향이 같은 경우
        patrol += abs(k-l)
    else:                               # 이동 방향이 다른 경우
        patrol += min(k+l, a - (k+l))

print(patrol)

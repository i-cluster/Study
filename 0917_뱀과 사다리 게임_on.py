# https://www.notion.so/20_09_17_BOJ16928-d7d140a2171e49adbf8729b2188bf6b9

n, m = map(int, input().split())
sec = [{}, {}]

for _ in range(n):
    x, y = map(int, input().split())
    sec[0][x] = y

for _ in range(m):
    u, v = map(int, input().split())
    sec[1][u] = v

# 이동 수 i, 탐색 중인 칸 p
i = 1
P = [1]
while max(P) < 94:
    # 주사위 굴리기
    i += 1
    # P에 저장된 칸들에서 탐색
    for j in range(len(P)):
        # 현재 칸 p
        p = P[j]
        # 주사위 이동 범위 1~6
        for k in range(1, 7):
            # 사다리 도착 지점 l, 뱀 도착 지점 s, 없으면 None
            l = sec[0].get(p+k)
            s = sec[1].get(p+k)
            # 사다리 찾기 : 1) 사다리가 있고 2) 도착 지점이 주사위 이동 거리보다 클 경우
            if l and l - p > 6:
                # 만약 도착 지점이 P 안에 없다면 P에 도착 지점 추가
                if l not in P: P.append(l)
            # 뱀 찾기 : 1) 뱀이 있고 2) 도착 지점이 탐색 칸들 중 가장 마지막이 아닐 경우
            elif s and s > min(P):
                # 만약 도착 지점이 P 안에 없다면 P에 도착 지점 추가
                if s not in P: P.append(s)
            # 아무것도 없는 칸일 경우
            else:
                # 주사위 최대 이동 거리 move 갱신
                move = k
        # 현재 칸을 move만큼 이동시키기
        P[j] += move

print(i)
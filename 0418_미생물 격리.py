# SWEA 2382
# https://bit.ly/3ggLsuN

# 격리 구역 sector, 미생물 위치 정보 micro
# 미생물 이동을 새 배열에 기록. [(미생물1 수, 방향 정보), (미생물2 수, 방향 정보) ...]
# micro를 순회하며 같은 위치에 있는 미생물 군집 결합

def quarantine(sec, mic):
    # 미생물 이동 후 격리 구역(결합 전)
    move = list([0] * n for _ in range(n))
    # 미생물 이동 후 위치
    new_mic = []
    for mi in mic:
        # 현재 위치 i j
        i, j = mi
        # 미생물 수 p, 방향 정보 di dj
        p, di, dj = sec[i][j]
        ni, nj = i + di, j + dj
        # 다음 위치가 약품 구역이면 방향 바꾸기
        if ni in (0, n-1) or nj in (0, n-1): p //= 2; di = -di; dj = -dj
        # 이동 구역에 미생물 정보 저장
        if move[ni][nj]: move[ni][nj].append((p, di, dj))
        else: move[ni][nj] = [(p, di, dj)]

        new_mic.append((ni, nj))

    # 중복 위치 제거
    new_mic = list(set(new_mic))
    # 미생물 이동 후 격리 구역(결합 후)
    new_sec = list([0] * n for _ in range(n))

    for mic in new_mic:
        i, j = mic
        # 최대 미생물 군집
        mp = max(move[i][j])
        # (전체 미생물 수, 최대 군집의 방향 정보)
        new_sec[i][j] = (sum(m[0] for m in move[i][j]), mp[1], mp[2])

    return new_sec, new_mic


d = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    # 격리 구역 크기 n, 격리 시간 m, 미생물 군집 수 k
    n, m, k = map(int, input().split())
    # 격리 구역 sector
    sector = list([0] * n for _ in range(n))
    # 미생물 위치 micro
    micro = []
    for _ in range(k):
        x, y, p, r = map(int, input().split())
        # 위치 정보 x y
        micro.append((x, y))
        # (미생물 수, 최대 미생물 군집, 방향 정보 d[r][0] d[r][1])
        sector[x][y] = (p, d[r][0], d[r][1])

    # m초 만큼 격리 구역과 미생물 위치 연산
    for _ in range(m):
        sector, micro = quarantine(sector, micro)

    print(f'#{tc} {sum(sector[mic[0]][mic[1]][0] for mic in micro)}')

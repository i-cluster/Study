# SWEA 5644
# https://bit.ly/2Qzcumk

# 이동 기록 move, bc 정보 bc, 충전량 btr
# 사용자 이동 후 bc 중심과의 거리 계산

d = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    # 이동 시간 m, bc 수 a
    m, a = map(int, input().split())
    # 이동 기록 - [A, B], 첫 이동 0 (현재 위치부터 시작)
    move = [(0,) + tuple(map(int, input().split())), (0,) + tuple(map(int, input().split()))]
    # bc 정보 - [bc1, bc2, bc3, ...]
    bc = [list(map(int, input().split())) for _ in range(a)]
    for b in bc:
        b[0] -= 1; b[1] -= 1

    # 사용자 위치 pos - [A, B], 배터리 btr
    pos, btr = [[0, 0], [9, 9]], 0
    for r in range(m+1):
        adj_bc = [[(-1, 0), (-1, 0)], [(-1, 0), (-1, 0)]]
        for k in range(2):
            # 이동하기
            di, dj = d[move[k][r]]
            pos[k][0] += di; pos[k][1] += dj

            # 인접 충전기 확인
            for l in range(a):
                # 충전기 좌표 i j, 충전 범위 c, 충전량 p
                i, j, c, p = bc[l]
                # 사용자 위치 x y
                x, y = pos[k]
                # 충전기와 사용자 거리가 충전 범위보다 작을 경우
                if abs(x-j) + abs(y-i) <= c: adj_bc[k].append((l, p))

        chrA = sorted(adj_bc[0], key= lambda x: x[1], reverse=True)
        chrB = sorted(adj_bc[1], key= lambda x: x[1], reverse=True)

        if chrA[0][0] != chrB[0][0]: btr += chrA[0][1] + chrB[0][1]
        else: btr += chrA[0][1] + max(chrA[1][1], chrB[1][1])

    print(f'#{tc} {btr}')
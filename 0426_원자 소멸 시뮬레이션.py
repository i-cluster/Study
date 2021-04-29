# SWEA 5648
# https://bit.ly/32NVThw

# 매초 원자를 이동시키며 충돌 여부를 확인
# 충돌 지점이 특정 좌표라면 충돌 기록을 남기고, 선상이라면 남기지 않음
# 모든 충돌 기록 지우고 다음 이동 시작
# 원자가 충돌 가능 범위(-1000, 1000) 바깥으로 나간다면 삭제

d = ((-1, 0), (1, 0), (0, -1), (0, 1))

import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    reactor = list([0] * 2001 for _ in range(2001))
    atoms = list()

    for _ in range(n):
        x, y, c, k = map(int, input().split())
        

    print(f'#{tc}')
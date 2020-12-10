# SWEA 6109

import sys
sys.stdin = open('sample.txt', 'r')


def game(x, y, k):
    # 이전 타일과 같으면 더하기
    if tile[y][x] == prev[1]:
        # 이전 타일 * 2
        tile[prev[0]][x] *= 2
        # 현재 타일 초기화
        tile[y][x] = 0
        # 다음 타일 값 초기화
        prev[1] = 0
    # 이전 타일과 다르면
    else:
        # 다음 타일 위치 +1
        prev[0] += k
        # 타일 값 기록
        prev[1] = tile[y][x]
        # 해당 위치로 타일 이동
        tile[prev[0]][x], tile[y][x] = tile[y][x], tile[prev[0]][x]


for tc in range(1, int(input())+1):
    n, s = map(str, input().split())
    n = int(n)
    tile = [list(map(int, input().split())) for _ in range(n)]

    if s == 'up':
        for i in range(n):
            # 이전타일 위치, 숫
            prev = [-1, 0]
            for j in range(n):
                # 타일 발견
                game(i, j, 1)
    else:
        for i in range(n-1, -1, -1):
            prev = [n, 0]
            for j in range(n-1, -1, -1):
                game(i, j, -1)

    print(f'#{tc}')
    print(n, s)
    for t in tile:
        print(t)
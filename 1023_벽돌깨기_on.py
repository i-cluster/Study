# SWEA 5656

# import sys
# sys.stdin = open('sample.txt', 'r')

from copy import deepcopy


def shoot(x, y):
    r = brick[x][y]
    d[x][y], brick[x][y] = 1, 0
    for i in range(-r+1, r):
        for dx, dy in [(x+i, y), (x, y+i)]:
            if 0 <= dx < h and 0 <= dy < w and not d[dx][dy]:
                if brick[dx][dy] > 1:
                    shoot(dx, dy)
                brick[dx][dy] = 0

        # if 0 <= y+i < w and not d[x][y+i]:
        #     if brick[x][y+i] > 1:
        #         shoot(x, y+i)
        #     brick[x][y+i] = 0


def search(i, j, n, brick):
    if n > 0:
        # (i, j)부터 탐색 시작
        while j < h:
            while i < w:
                if brick[j][i] > 1:
                    # 원본 복사
                    brickcopy = deepcopy(brick)
                    # 구슬 수
                    c = 1
                    while j > 0 and brick[j-1][i]:
                        # 2칸 이상 벽돌 있으면 넘어가기
                        if brick[j-1][i] > 1: break
                        c += 1; j -= 1
                    else:
                        j += c-1
                        # 필요한 구슬보다 남은 구슬이 많을 경우
                        if n >= c:
                            # 구슬 쏘기
                            shoot(j, i)
                            # 아래로 쌓기
                            for x in range(w):
                                height = h - 1
                                for y in range(h - 1, -1, -1):
                                    if brick[y][x]:
                                        brick[height][x], brick[y][x] = brick[y][x], brick[height][x]
                                        height -= 1
                            # 다음 탐색
                            search(i+1, j, n-c, brick)
                            # 쏘지 않고 지나가기
                            brick = brickcopy
                i += 1

            j += 1; i = 0

    else:
        cnt = 0
        for y in range(h):
            for x in range(w):
                if brick[y][x]: cnt += 1
        global min_brick
        if cnt < min_brick:
            min_brick = cnt


for tc in range(1, int(input())+1):
    n, w, h = map(int, input().split())
    brick = [list(map(int, input().split())) for _ in range(h)]

    d = [[0] * w for _ in range(h)]
    min_brick = w * h

    search(0, 0, n, brick)

    print(f'#{tc} {min_brick}')


    # shoot(2, 2)
    #
    # # 아래부터 쌓기
    # for i in range(w):
    #     height = h-1
    #     for j in range(h-1, -1, -1):
    #         if brick[j][i]:
    #             brick[height][i], brick[j][i] = brick[j][i], brick[height][i]
    #             height -= 1
    #
    # print()
    # for b in brick:
    #     print(b)

'''
1
3 10 10
0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 0 0 0 0
1 0 3 0 1 1 0 0 0 1
1 1 1 0 1 2 0 0 0 9
1 1 4 2 1 1 0 0 1 1
1 1 4 2 1 1 2 1 1 1
1 1 5 1 1 1 1 2 1 1
1 1 6 1 1 1 1 1 2 1
1 1 1 1 1 1 1 1 1 5
1 1 7 1 1 1 1 1 1 1
2 9 10
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0
1 1 0 0 1 0 0 0 0
1 1 0 1 1 1 0 1 0
1 1 0 1 1 1 0 1 0
1 1 1 1 1 1 1 1 0
1 1 3 1 6 1 1 1 1
1 1 1 1 1 1 1 1 1
'''
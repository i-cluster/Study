# SWEA 4615
# https://bit.ly/3aGQi12

d = [0, 1, 0, -1, -1, 1, 1, -1, 0]


def turn(i, j, c):
    for k in range(8):
        di, dj = i + d[k], j + d[k+1]
        st = []

        # 범위 내 탐색
        while 0 <= di < n and 0 <= dj < n:
            # 같은 돌 만났을 때
            if board[di][dj] == c:
                for s in st:
                    board[s[0]][s[1]] = c
                break
            # 다른 돌 만났을 때
            elif board[di][dj] + c == 3:
                st.append((di, dj))
                di += d[k]; dj += d[k+1]
            # 그냥 빈 공간일 때
            else: break


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[n//2 - 1][n//2 - 1:n//2 + 1], board[n//2][n//2 - 1:n//2 + 1] = [2, 1], [1, 2]

    for _ in range(m):
        y, x, c = map(lambda x: int(x) - 1, input().split())
        board[x][y] = c+1
        turn(x, y, c+1)

    print(f'#{tc} {sum(br.count(1) for br in board)} {sum(br.count(2) for br in board)}')
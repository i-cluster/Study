# https://www.acmicpc.net/problem/2578

bingo = [list(map(int, input().split())) for _ in range(5)]

win = [5, [5] * 5, [5] * 5, 5]

cnt = 0
for p in range(5):
    num = list(map(int, input().split()))
    for n in num:
        # 행 탐색으로 번호 찾기
        for k in range(5):
            # 번호 찾으면
            if n in bingo[k]:
                # 열 번호 추출
                y = bingo[k].index(n)
                # 행에서 남은 번호 -1하고 0이면 count +1
                win[1][k] -= 1
                if not win[1][k]: cnt += 1
                # 열에서 남은 번호 -1하고 0이면 count +1
                win[2][y] -= 1
                if not win[2][y]: cnt += 1

                # 행과 열 번호가 같으면 정방향 대각선 남은 번호 -1하고 0이면 count +1
                if y == k:
                    win[0] -= 1
                    if not win[0]: cnt += 1
                # 행과 열 번호 합이 4면 역방향 대각선 남은 번호 -1하고 0이면 count +1
                if y + k == 4:
                    win[-1] -= 1
                    if not win[-1]: cnt += 1

                # 찾았으니까 탐색 종료
                break

        if cnt >= 3:
            print(p * 5 + num.index(n) + 1)
            break
    if cnt >= 3: break
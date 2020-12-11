# JO 1671

board = [list(0 for _ in range(100)) for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        board[i][y:y+10] = [1] * 10

Round = 0
for i in range(100):
    r, c = 0, 0
    for j in range(100):
        if board[i][j] != r:
            Round += 1
            r = board[i][j]
        if board[j][i] != c:
            Round += 1
            c = board[j][i]
    else:
        if board[i][99]: Round += 1
        if board[99][i]: Round += 1

print(Round)
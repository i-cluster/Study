# SWEA 1974
# https://bit.ly/3b0tdXj

def test():
    for i in range(9):
        data = [[0] * 10 for _ in range(3)]
        for j in range(9):
            if not data[0][sudoku[i][j]]: data[0][sudoku[i][j]] = 1
            else: return 0

            if not data[1][sudoku[j][i]]: data[1][sudoku[j][i]] = 1
            else: return 0

            if not data[2][sudoku[(i % 3) * 3 + (j // 3)][j % 3]]: data[2][sudoku[(i % 3) * 3 + (j // 3)][j % 3]] = 1
            else: return 0

    return 1


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {test()}')
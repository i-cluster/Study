# SWEA 1961

def spin(k):
    for i in range(n):
        for j in range(n):
            spin_arr[j][k] = arr[i][j] + spin_arr[j][k]

    for i in range(n):
        arr[i] = spin_arr[i][k]


for tc in range(1, int(input())+1):
    n = int(input())

    arr = [list(map(str, input().split())) for _ in range(n)]
    spin_arr = [[''] * n for _ in range(n)]

    for k in range(3):
        spin(k)

    print(f'#{tc}')
    for i in range(n):
        print(' '.join(spin_arr[i]))






'''
2
3
1 2 3
4 5 6
7 8 9
6
6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
'''
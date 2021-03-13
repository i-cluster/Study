# SWEA 4014
# https://bit.ly/3lcUp8F

def construct(arr, x):
    global runway
    j, l = 0, 1
    while j < n-1:
        if arr[j] == arr[j+1]: l += 1
        else:
            if -1 <= arr[j] - arr[j+1] <= 1:
                # 오르막길
                if arr[j] - arr[j+1] == -1:
                    if l < x: return
                    l = 1
                # 내리막길
                else:
                    for _ in range(x-1):
                        j += 1
                        if j + 1 >= n or arr[j] != arr[j + 1]: return
                    l = 0
            else: return
        j += 1

    runway += 1


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, x = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(n)]

    runway = 0
    for i in range(n):
        construct(field[i], x)
        construct(list(field[j][i] for j in range(n)), x)

    print(f'#{tc} {runway}')
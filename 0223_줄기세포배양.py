# SWEA 5653
# https://bit.ly/3aGQi12

# 빈자리 '0', 비활성화 > 0, 활성화 < 0, 죽은 세포 = ''

from copy import deepcopy

d = [0, 1, 0, -1, 0]

# 번식
def breeding(arr):
    for ar in arr:
        i, j, p = ar[0], ar[1], ar[2]
        for k in range(4):
            di, dj = i + d[k], j + d[k+1]
            if cont[di][dj] and type(cont[di][dj]) == str and p > int(cont[di][dj]):
                cont[di][dj] = str(p)
                cell[(di, dj)] = p

# 배양
def culture(dic):
    arr = []
    for d in dic.keys():
        i, j = d[0], d[1]
        # 고정 해제
        if type(cont[i][j]) == str: cont[i][j] = int(cont[i][j])
        # 번식할 세포 리스트 업데이트
        if not cont[i][j]: arr.append((i, j, dic[d]))
        # 생명력 감소
        cont[i][j] -= 1
        # 세포 사망
        if cont[i][j] == -dic[d]:
            cont[i][j] = ''
            del cell[d]

    breeding(arr)


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    cont = [['0'] * (m+k) for _ in range(n+k)]
    # 탐색할 세포 리스트
    cell = dict()

    lenx, leny = (n+k)//2 - n//2, (m+k)//2 - m//2
    for x in range(lenx, lenx + n):
        arr = list(input().split())
        for y in range(m):
            if int(arr[y]): cell[(x, leny + y)] = int(arr[y])
        cont[x][leny:leny + m] = arr

    while k:
        culture(deepcopy(cell))
        k -= 1

    print(f'#{tc} {len(cell.keys())} {cell}')
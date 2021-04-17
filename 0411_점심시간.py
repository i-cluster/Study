# SWEA 2383
# https://bit.ly/3sb5IjH

# 사람마다 어느 출구로 나갈지 배정
# 시뮬레이션 돌려보기

def run(e):
    out = []
    for i in range(2):
        line, tm = e[i], exit[i][2]
        if line:
            line.sort()

            # 계단을 다 내려간 시간
            arrival = [line[i] + 1 + tm for i in range(min(3, len(line)))]

            i = 3
            # 전부 계단을 내려갈 때까지 반복
            while i < len(line):
                x, y = arrival.pop(0), line[i]
                # 대기자 없을 경우
                if y >= x: arrival.append(y + tm + 1)
                # 대기자 있을 경우
                else: arrival.append(x + tm)
                i += 1

            out.append(arrival[-1])

    global ans
    m = max(out)
    if m < ans: ans = m


def simulation(i, exit1, exit2):
    if i == p: run([exit1, exit2])
    else:
        x, y = peop[i]
        simulation(i+1, exit1 + [abs(x - exit[0][0]) + abs(y - exit[0][1])], exit2)
        simulation(i+1, exit1, exit2 + [abs(x - exit[1][0]) + abs(y - exit[1][1])])


import sys
sys.stdin = open('sample.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    room = []

    peop, exit = [], []
    for r in range(n):
        arr = list(map(int, input().split()))
        for c in range(n):
            if arr[c] > 1: exit.append((r, c, arr[c]))
            elif arr[c]: peop.append((r, c))
        room.append(arr)

    ans = (n ** 2) * 10

    # 출구 배정
    p = len(peop)
    simulation(0, [], [])

    print(f'#{tc} {ans}')